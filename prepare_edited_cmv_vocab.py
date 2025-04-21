import argparse
from datasets import load_dataset
import os

def parse_args():
    parser = argparse.ArgumentParser(description="Prepare vocabulary for F5-TTS finetuning")
    parser.add_argument(
        "--base_vocab_path",
        type=str,
        required=True,
        help="Path to the pretrained model's vocabulary file"
    )
    parser.add_argument(
        "--output_path",
        type=str,
        required=True,
        help="Path to save the extended vocabulary file"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    
    # Load the dataset
    dataset = load_dataset("ThuraAung1601/edited-common-voice-with-ipa", split="train")

    # Extract unique IPA symbols
    vocab_set = set()
    for item in dataset:
        vocab_set.update(list(item['ipa_sentence']))

    # Get the base vocab from pretrained model
    with open(args.base_vocab_path, "r", encoding="utf-8-sig") as f:
        base_vocab = set(f.read().split("\n"))

    # Combine and sort
    all_vocab = sorted(base_vocab.union(vocab_set))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(all_vocab))

if __name__ == "__main__":
    main()