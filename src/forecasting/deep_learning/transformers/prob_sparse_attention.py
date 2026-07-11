import math

import torch
import torch.nn as nn


class ProbSparseAttention(nn.Module):

    def __init__(
        self,
        d_model=64,
        n_heads=4,
    ):

        super().__init__()

        self.attention = nn.MultiheadAttention(
            embed_dim=d_model,
            num_heads=n_heads,
            batch_first=True,
        )

    def forward(self, x):

        batch_size, seq_len, d_model = x.shape

        # Number of important queries to keep
        u = max(
            1,
            int(math.log2(seq_len))
        )

        # L2 norm used as a simple importance score
        scores = torch.norm(
            x,
            dim=-1,
        )

        top_queries = torch.topk(
            scores,
            k=u,
            dim=1,
        ).indices

        sparse_x = torch.gather(
            x,
            dim=1,
            index=top_queries.unsqueeze(-1).expand(
                -1,
                -1,
                d_model,
            ),
        )

        output, _ = self.attention(
            sparse_x,
            x,
            x,
        )

        pooled = output.mean(
            dim=1,
            keepdim=True,
        )

        pooled = pooled.repeat(
            1,
            seq_len,
            1,
        )

        return pooled