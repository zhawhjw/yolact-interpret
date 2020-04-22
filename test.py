import torch

if __name__ == "__main__":
    torch.cuda.is_available()
    torch.cuda.current_device()