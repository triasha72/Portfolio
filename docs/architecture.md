# Site architecture

```mermaid
flowchart LR
    A[Repository result artifacts] --> B[Manual evidence check]
    B --> C[Project case-study pages]
    D[Shared CSS] --> C
    E[Project figures] --> C
    C --> F[Static portfolio site]
    G[Resume source] --> H[Downloadable PDF]
    H --> F
```

The site is intentionally static. Project pages summarize checked-in repository
results, while the repositories remain the source of record. Shared styles keep
the pages consistent without adding a JavaScript framework or build pipeline.

When a project result changes, update the repository artifact first, then its
case study, profile README, and resume. That order prevents the portfolio from
claiming work that the linked repository does not support.
