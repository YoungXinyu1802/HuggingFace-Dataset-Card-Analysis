# Full FLIP stability dataset

The stability dataset from flip, which is based on the meltome atlas, data has those columns:

```
[ 'index', 'seq_id', 'sequence', 'target', 'cluster_center',
       'cluster_distance']
       ```
       
- **Index** from the original dataset
- **Seq_id** a unique sequence ID string that is concatenated from several other IDs (also Unirep)
- **Sequence** The actual protein sequence as a string
- **Target** the melting point temperature of the protein TM 
- **Cluster center** The seq_id of the cluster center protein this sequence is assigned to. Can also be its won seq_id if this sequence is a center.
- **Cluster distance** The levenstein distance of the protein to its cluster center.