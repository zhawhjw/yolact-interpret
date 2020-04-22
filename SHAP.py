import torch

e1 = "/home/hao/Downloads/eval_yes/0_1_10.pt"
e2 = "/home/hao/Downloads/eval_yes/0_2_6.pt"
if __name__ == "__main__":
    x = torch.load(e1)

    print(x)

    x = torch.load(e2)

    print(x)

