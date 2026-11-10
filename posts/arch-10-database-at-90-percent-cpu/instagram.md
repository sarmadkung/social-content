Your database is at 90% CPU. The app servers are at 30%. Launch is next week. What do you try first?

The slides go in order, cheapest and safest first: measure, fix the query and add the index, cache hot reads, read replicas, scale up, and only then shard.

The one to remember: it is often just one query. Fix the query before you fix the architecture.

Swipe →

#systemdesign #databases #postgresql #performance #softwarearchitecture
