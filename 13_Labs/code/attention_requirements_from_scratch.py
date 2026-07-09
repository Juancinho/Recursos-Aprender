"""
Didactic cross-attention between two requirements.

This script uses random reproducible token embeddings. The attention matrices are useful
to understand Q/K/V mechanics, but they do not encode real semantics.
"""
from pathlib import Path
import re
import math

try:
    import torch
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError as exc:
    print("Missing dependency:", exc)
    print("Install with: pip install torch pandas matplotlib")
    raise SystemExit(1)

REQ_A = "The ECU shall support UDS service 0x22 ReadDataByIdentifier."
REQ_B = "The diagnostic module shall return NRC 0x31 when the DID is unsupported."
OUT = Path(__file__).resolve().parents[1] / "outputs"
OUT.mkdir(parents=True, exist_ok=True)

def tokenize(text):
    return re.findall(r"0x[0-9A-Fa-f]+|[A-Za-z_]+|\d+", text)

def scaled_dot_product_attention(Q, K, V):
    d_k = Q.shape[-1]
    scores = Q @ K.T / math.sqrt(d_k)
    weights = torch.softmax(scores, dim=-1)
    output = weights @ V
    return output, weights

def cross_attention(tokens_a, tokens_b, d_model=16, d_k=12):
    vocab = sorted(set(tokens_a + tokens_b))
    token_to_vec = {tok: torch.randn(d_model) for tok in vocab}
    X_a = torch.stack([token_to_vec[t] for t in tokens_a])
    X_b = torch.stack([token_to_vec[t] for t in tokens_b])
    W_Q = torch.randn(d_model, d_k)
    W_K = torch.randn(d_model, d_k)
    W_V = torch.randn(d_model, d_k)
    Q_a = X_a @ W_Q
    K_b = X_b @ W_K
    V_b = X_b @ W_V
    _, weights = scaled_dot_product_attention(Q_a, K_b, V_b)
    return weights

def save_heatmap(weights, rows, cols, path, title):
    df = pd.DataFrame(weights.detach().numpy(), index=rows, columns=cols)
    print(f"\n{title}")
    print(df.round(3))
    plt.figure(figsize=(max(8, len(cols) * 0.7), max(4, len(rows) * 0.45)))
    plt.imshow(df.values, aspect="auto", cmap="viridis")
    plt.colorbar(label="attention weight")
    plt.xticks(range(len(cols)), cols, rotation=45, ha="right")
    plt.yticks(range(len(rows)), rows)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(path, dpi=160)
    plt.close()
    print(f"Saved {path}")

def main():
    torch.manual_seed(42)
    tokens_a = tokenize(REQ_A)
    tokens_b = tokenize(REQ_B)
    w_ab = cross_attention(tokens_a, tokens_b)
    w_ba = cross_attention(tokens_b, tokens_a)
    save_heatmap(w_ab, tokens_a, tokens_b, OUT / "attention_a_to_b.png", "Requirement A attends to B")
    save_heatmap(w_ba, tokens_b, tokens_a, OUT / "attention_b_to_a.png", "Requirement B attends to A")

if __name__ == "__main__":
    main()
