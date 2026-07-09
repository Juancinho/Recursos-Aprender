from pathlib import Path

try:
    import numpy as np
    import pandas as pd
    import torch
    from torch import nn
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import classification_report
except ImportError as exc:
    print("Missing dependency:", exc)
    print("Install with: pip install torch pandas numpy scikit-learn")
    raise SystemExit(1)

OUT = Path(__file__).resolve().parents[1] / "outputs"
OUT.mkdir(parents=True, exist_ok=True)
CSV = OUT / "can_synthetic.csv"

def make_dataset(n_normal=3000, n_anom=120):
    rng = np.random.default_rng(42)
    ids = np.array([0x120, 0x220, 0x321])
    rows = []
    t = 0.0
    for _ in range(n_normal):
        can_id = int(rng.choice(ids, p=[0.5, 0.3, 0.2]))
        dlc = 8
        delta = float(rng.normal(0.010 if can_id == 0x120 else 0.020, 0.001))
        t += max(delta, 0.001)
        base = {
            0x120: [10, 20, 30, 40, 50, 60, 70, 80],
            0x220: [1, 2, 3, 4, 5, 6, 7, 8],
            0x321: [100, 90, 80, 70, 60, 50, 40, 30],
        }[can_id]
        payload = np.clip(np.array(base) + rng.normal(0, 2, 8), 0, 255).astype(int)
        rows.append([t, can_id, dlc, delta, *payload, 0])
    for _ in range(n_anom):
        can_id = int(rng.choice([0x120, 0x999, 0x220]))
        dlc = int(rng.choice([4, 8]))
        delta = float(rng.uniform(0.0001, 0.08))
        t += delta
        payload = rng.integers(0, 256, 8)
        rows.append([t, can_id, dlc, delta, *payload, 1])
    cols = ["timestamp", "can_id_int", "dlc", "delta_time"] + [f"b{i}" for i in range(8)] + ["label"]
    df = pd.DataFrame(rows, columns=cols).sample(frac=1, random_state=42).reset_index(drop=True)
    df.to_csv(CSV, index=False)
    return df

class AutoEncoder(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(dim, 16), nn.ReLU(),
            nn.Linear(16, 4), nn.ReLU(),
            nn.Linear(4, 16), nn.ReLU(),
            nn.Linear(16, dim),
        )
    def forward(self, x):
        return self.net(x)

def main():
    torch.manual_seed(42)
    df = pd.read_csv(CSV) if CSV.exists() else make_dataset()
    features = ["can_id_int", "dlc", "delta_time"] + [f"b{i}" for i in range(8)]
    normal = df[df.label == 0]
    scaler = StandardScaler()
    X_train = scaler.fit_transform(normal[features])
    X_all = scaler.transform(df[features])
    x_train = torch.tensor(X_train, dtype=torch.float32)
    x_all = torch.tensor(X_all, dtype=torch.float32)
    model = AutoEncoder(x_train.shape[1])
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = nn.MSELoss()
    for epoch in range(30):
        opt.zero_grad()
        recon = model(x_train)
        loss = loss_fn(recon, x_train)
        loss.backward()
        opt.step()
        if epoch in {0, 9, 19, 29}:
            print(f"epoch={epoch+1:02d} loss={loss.item():.6f}")
    with torch.no_grad():
        train_err = ((model(x_train) - x_train) ** 2).mean(dim=1).numpy()
        all_err = ((model(x_all) - x_all) ** 2).mean(dim=1).numpy()
    threshold = np.percentile(train_err, 99)
    pred = (all_err > threshold).astype(int)
    print(f"Threshold p99 normal reconstruction error: {threshold:.6f}")
    print(classification_report(df.label.values, pred, target_names=["normal", "anomaly"]))
    out = df.copy()
    out["reconstruction_error"] = all_err
    out["pred_anomaly"] = pred
    path = OUT / "can_autoencoder_scored.csv"
    out.to_csv(path, index=False)
    print(f"Saved {path}")

if __name__ == "__main__":
    main()
