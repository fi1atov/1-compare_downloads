### Results of different programming
|                        | 10     | 50      | 100     |
|------------------------|--------|---------|---------|
| Sync                   | 7.1878 | 42.1648 | 76.2423 |
| Async with aiofiles    | 1.5986 | 4.3172  | 6.9309  |
| Async without aiofiles | 2.2327 | 4.2621  | 7.9700  |
| Threads                | 2.6349 | 7.8066  | 14.1082 |
| Processes              | 0.9550 | 3.8093  | 8.5058  |