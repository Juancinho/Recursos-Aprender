"""
Extract token attentions from a small Transformer model for a pair of requirements.

Attention is not causal explanation. Treat the heatmap as an inspection tool.
"""
from pathlib import Path

try:
    import torch
    import pandas as pd
    import matplotlib.pyplot as plt
    from transformers import AutoTokenizer, AutoModel
except ImportError as exc:
    print("Missing dependency:", exc)
    print("Install with: pip install transformers torch matplotlib pandas")
    raise SystemExit(1)

REQ_A = "The ECU shall support UDS service 0x22 ReadDataByIdentifier."
REQ_B = "The diagnostic module shall return NRC 0x31 when the DID is unsupported."
MODEL_NAME = "distilbert-base-uncased"
OUT = Path(__file__).resolve().parents[1] / "outputs"
OUT.mkdir(parents=True, exist_ok=True)

def main():
    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModel.from_pretrained(MODEL_NAME, output_attentions=True)
    except Exception as exc:
        print("Could not load model. If this is the first run, internet/cache may be required.")
        print("Model:", MODEL_NAME)
        print("Error:", exc)
        raise SystemExit(1)

    encoded = tokenizer(REQ_A, REQ_B, return_tensors="pt")
    tokens = tokenizer.convert_ids_to_tokens(encoded["input_ids"][0])
    token_type_ids = encoded.get("token_type_ids")
    # DistilBERT may not return token_type_ids. Split by [SEP] instead.
    sep_positions = [i for i, tok in enumerate(tokens) if tok == "[SEP]"]
    if len(sep_positions) < 2:
        print("Could not identify pair boundary.")
        raise SystemExit(1)
    a_start, a_end = 1, sep_positions[0]
    b_start, b_end = sep_positions[0] + 1, sep_positions[1]

    with torch.no_grad():
        outputs = model(**encoded)

    # attentions: tuple(layers), each [batch, heads, seq, seq]
    attentions = outputs.attentions
    layer_idx = -1
    head_idx = 0
    matrix = attentions[layer_idx][0, head_idx, a_start:a_end, b_start:b_end]
    rows = tokens[a_start:a_end]
    cols = tokens[b_start:b_end]

    df = pd.DataFrame(matrix.numpy(), index=rows, columns=cols)
    csv_path = OUT / "transformer_attention_a_to_b.csv"
    png_path = OUT / "transformer_attention_a_to_b.png"
    df.to_csv(csv_path)

    plt.figure(figsize=(max(8, len(cols) * 0.65), max(4, len(rows) * 0.45)))
    plt.imshow(df.values, aspect="auto", cmap="magma")
    plt.colorbar(label="attention weight")
    plt.xticks(range(len(cols)), cols, rotation=45, ha="right")
    plt.yticks(range(len(rows)), rows)
    plt.title(f"{MODEL_NAME}: layer {layer_idx}, head {head_idx}, A -> B")
    plt.tight_layout()
    plt.savefig(png_path, dpi=160)
    plt.close()

    print(f"Layers: {len(attentions)}")
    print(f"Heads in selected layer: {attentions[layer_idx].shape[1]}")
    print(f"Saved {csv_path}")
    print(f"Saved {png_path}")
    print("Reminder: attention weights are not causal explanations.")

if __name__ == "__main__":
    main()
