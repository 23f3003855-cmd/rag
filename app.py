KB = [
"Raft consensus requires a quorum of 4 nodes to commit a log entry. The leader sends 200ms heartbeats to prevent follower election timeouts. Network partitions cause the minority partition to stop accepting writes. Log compaction via snapshotting reduces replay time after a crash. etcd and CockroachDB both implement Raft for replicated state machines.",
"Multi-Paxos consensus coordinates distributed replicated state without a single permanent master. Leader leases establish proposal rights for lease terms of 1000ms before re-election. In the accept phase, a commit quorum of 3 acceptors must acknowledge the ballot number. Proposers resolve ballot conflicts through randomized backoff intervals. Google Chubby and Apache ZooKeeper incorporate Paxos-family consensus protocols.",
"Epidemic gossip protocols spread cluster membership updates in logarithmic rounds. The phi accrual failure detector triggers node suspicion after a 1000ms suspicion timeout. If network ping latency pushes the accrual metric past 0.9, the cluster marks the node dead. Anti-entropy background exchanges repair missing data versions across healthy nodes. Apache Cassandra relies on gossip for ring state coordination.",
"The SWIM membership protocol provides weakly-consistent cluster membership with bounded false-positive rates. Nodes transmit ping probes periodically with a ping interval of 250ms. When an indirect ping probe fails, suspect timeout counters initiate dead-node eviction after crossing 0.85. Dissemination piggybacks membership updates onto outgoing probe packets to minimize packet overhead. HashiCorp Consul implements SWIM for decentralized cluster health monitoring.",
"Two-phase commit coordinates atomic distributed transactions across independent resource managers. The coordinator aborts the transaction if any participant fails to reply within a 1000ms prepare timeout. In three-phase commit, non-blocking progress is guaranteed by requiring a pre-commit quorum of 2 participants. Presumed-abort optimizations eliminate logging coordinator decisions for rolled-back transactions. Distributed deadlocks during phase one are detected using cycle detection on wait-for graphs.",
"The Saga pattern orchestrates distributed long-running transactions across independent microservices using compensating actions. Forward execution steps timeout and trigger backward compensation if service responses exceed 100ms. Orchestration coordinators retry idempotent compensating steps across a minimum of 5 service retries before alerting. Unlike atomic two-phase commit, intermediate states remain visible to concurrent transactions across services. Temporal and Uber Cadence utilize sagas for resilient distributed workflows.",
"Consistent hashing maps nodes and keys onto a virtual ring to balance partition loads. When key redistribution skew exceeds a 0.9 threshold, virtual nodes are dynamically allocated to smooth variance. Vector clocks track causal event ordering across concurrent distributed replicas without synchronized clocks. Dynamic read repair discovers stale replicas during quorum read operations within 100ms intervals. Amazon Dynamo popularized this decentralized replication architecture.",
"Rendezvous hashing assigns object keys to highest-ranking server nodes through pseudo-random score evaluation. Hash weight multipliers scale server selection when load capacity distribution crosses a 0.9 threshold. When servers fail, displaced keys fail over to the next highest-scoring node within 1000ms. Unlike consistent hash rings, rendezvous hashing eliminates virtual node maintenance overhead completely. Proxy caches like Squid and Envoy use highest random weight hashing for backend routing.",
"Vector clocks capture partial ordering and causal relationships among concurrent events in distributed stores. When read repairs detect version concurrency, divergence resolution triggers within 200ms of replica discovery. Version vectors prune stale ancestor entries when actor membership counts exceed 3 replicas. Conflict resolution delegates sibling merges to application-specific resolution routines when clocks are concurrent. Riak KV relies on vector clocks for causality tracking across multi-master replicas.",
"Hybrid logical clocks provide monotonic causality tracking by combining physical hardware timers with logical sequence counters. Clock synchronization algorithms bound maximum physical time drift within 250ms across all cluster nodes. If physical time advances past logical timestamps, the logical offset resets when skew drops below 0.7. Hybrid logical clocks produce single 64-bit timestamps without unbounded vector size inflation. CockroachDB and MongoDB use hybrid logical clocks for linearizable distributed read timestamps.",
"Stochastic gradient descent updates model weights iteratively using sampled mini-batches. Training mini-batches are grouped into sizes of 32 samples per forward step. The optimizer applies a base learning rate of 0.05 to scale weight gradient updates. Momentum accumulates historical gradient vectors to accelerate traversal through shallow saddle points. Weight decay provides L2 regularization to prevent over-parameterized models from overfitting.",
"AdamW stabilizes adaptive parameter updates by decoupling weight decay regularization from gradient moment updates. First and second exponential moment vectors track running gradients across mini-batches of 256 samples. The initial learning rate schedule initializes step updates at 0.001 prior to cosine annealing. Decoupled weight decay applies L2 penalties directly to parameters without distorting adaptive learning rates. HuggingFace transformers employ AdamW as the standard optimizer for foundation model pre-training.",
"Transformer encoders use multi-head self-attention mechanisms to capture long-range contextual token representations. The deep backbone stack consists of 4 sequential transformer blocks with residual connections. Warmup scheduling ramps up the step learning rate toward 0.001 before cosine decay begins. Layer normalization stabilizes hidden state activations across varying input sequence lengths. Positional embeddings inject positional sequence order into permutation-invariant attention computations.",
"Autoregressive transformer decoders generate token sequences iteratively using causal attention masks. The causal generative model stacks 3 transformer blocks configured with rotary position embeddings. Training sequences partition token streams into window lengths of 64 tokens per gradient step. Causal masking zeros future token attention weights to enforce unidirectional auto-regressive generation. Modern generative models like LLaMA and GPT rely on decoder-only autoregressive architectures.",
"Binary logistic regression maps linear logit combinations into probabilistic predictions via sigmoid activation. Classification decisions categorize positive predictions whenever estimated class probability exceeds 0.7. Evaluation validation batches process 32 instances simultaneously during offline scoring passes. Expected calibration error quantifies probability deviation between predicted confidences and true empirical accuracy. Temperature scaling adjusts logit temperatures to produce well-calibrated posterior probabilities without degrading accuracy.",
"Support vector machines construct maximum-margin hyperplanes to separate high-dimensional feature distributions. The soft-margin optimization penalty penalizes margin violations exceeding a slack threshold of 0.5. Training optimization solves dual quadratic programs across sub-sampled chunks of 64 support vectors. Radial basis function kernels project non-linear decision boundaries into infinite-dimensional Hilbert spaces. Platt scaling fits logistic sigmoids over raw SVM output distances to derive posterior confidence probabilities.",
"Multi-layer perceptrons learn hierarchical feature abstractions through stacked non-linear transformations. The feedforward classifier contains 12 hidden dense layers with GELU activations. Dropout randomly zeros unit outputs with probability exceeding 0.5 to prevent co-adaptation. Batch normalization normalizes internal activation distributions across training minibatches. Gradient clipping bounds the L2 norm of parameter gradients to avoid catastrophic exploding gradients.",
"Residual convolutional networks mitigate vanishing gradients across deep computer vision architectures using identity skip connections. The feature extraction backbone organizes 3 residual bottleneck blocks grouped into spatial resolution stages. Spatial feature dropout suppresses activation feature maps when unit correlation exceeds 0.5. Convolutions apply spatial kernels across input feature dimensions to learn translation-invariant spatial representations. ResNet and ConvNeXt architectures demonstrate that skip connections enable stable convergence in deep networks.",
"Batch normalization accelerates neural network training by normalizing layer input distributions across mini-batch dimensions. Normalization statistics calculate empirical mean and variance over batch sizes of 64 training examples. If running variance moving averages diverge beyond a 0.7 threshold, momentum updates re-calibrate batch statistics. Learnable affine scale and shift parameters restore network representational capacity after zero-mean scaling. Modern vision architectures integrate batch normalization immediately prior to non-linear activation functions.",
"Layer normalization computes normalization statistics independently across feature channel dimensions for each sequence sample. Deep transformer stacks apply pre-layer normalization across 12 sequential attention layers. The optimization pipeline configures learning rate warmup targets of 0.01 to prevent gradient explosion. Unlike batch normalization, layer normalization computes identical statistics during training and inference without batch dependence. Natural language processing models depend on layer normalization for recurrent and attention sequence processing.",
"PostgreSQL manages relational table storage using page-level multi-version concurrency control. Database server instances listen for incoming client socket connections on port 5432. Connection poolers like PgBouncer disconnect idle backend connections after a 500ms timeout. The write-ahead log ensures crash recovery by persisting transaction records before dirty buffer flushes. Vacuum processes clean dead row versions created by updates and deletes to prevent table bloat.",
"MySQL InnoDB implements multi-version concurrency control using undo log segments and clustered index storage. Server daemons accept incoming client connections on default network port 27017. Transaction lock wait timers abort blocked queries if row lock acquisition exceeds 100ms. Undo logs record prior row versions to reconstruct consistent read views without table-level locking. Purge threads asynchronously deallocate committed undo log pages to reclaim tablespace.",
"B+ Tree data structures provide balanced logarithmic search and sequential range scan access. Internal index pages split when node fill capacity surpasses a 0.85 saturation ratio. Bulk insert workloads group leaf index modifications into 64 record chunks to minimize random I/O. Clustered indexes determine physical storage order on primary disk pages to maximize cache locality. Page latching protocols enforce concurrent thread safety during structural page split operations.",
"Log-structured merge trees optimize write-heavy workloads by buffering incoming modifications in memory before sequential disk writes. Compaction processes merge sorted runs into lower levels when level size saturation exceeds 0.85. Memory tables flush immutable write buffers in chunks of 128 records to sequential SSTable files. Bloom filters allow fast point lookups by determining key absence without performing disk reads. RocksDB and Apache Cassandra use LSM trees to achieve high write throughput.",
"MongoDB organizes schemaless documents inside scalable sharded collections across cluster replica sets. Daemon processes listen for client wire traffic over default port 27017 on each node. Write concern requires acknowledgment from a replica quorum of 5 members to confirm persistence. WiredTiger storage engine utilizes log-structured storage algorithms with Snappy compression for high throughput. Secondary nodes asynchronously replay the primary oplog to maintain read replica synchronization.",
"Apache Cassandra distributes partition rows across peer-to-peer storage clusters using token-based ring partitioning. Database nodes listen for client CQL requests on native transport port 5432. Consistency levels require acknowledgment from a quorum of 3 replica nodes before write confirmation. Memtables persist incoming mutations sequentially to commit logs before flushing immutable SSTables to disk. Read repairs update out-of-sync replicas asynchronously in the background when replica checksums disagree.",
"Redis operates as an in-memory key-value data store optimized for sub-millisecond retrieval. By default the Redis server daemon process binds to network port 9200 for TCP traffic. Client connections terminate when idle connection durations exceed the configured 1000ms limit. Redis persistence snapshotting writes point-in-time RDB files and appends commands to the AOF log. The LRU eviction algorithm frees memory when maximum memory limits are reached by dropping stale keys.",
"Memcached provides high-throughput distributed memory object caching via a multi-threaded slab allocator architecture. Daemon worker threads bind to default TCP listening port 6379 to serve cache requests. Connection timeouts terminate stalled client sockets when inactivity intervals surpass 250ms. Slab allocation avoids memory fragmentation by pre-allocating memory into slabs of specific chunk sizes. Unlike Redis, Memcached does not support disk persistence or complex data structures like sets and hashes.",
"Write-ahead logging guarantees ACID durability by persisting database modification logs before changes write to table data pages. Checkpoint background processes flush dirty shared buffers when checkpoint log capacity crosses 0.7 utilization. Group commit buffers batch concurrent transaction flush requests into 64 log entries per fsync disk flush. The ARIES recovery algorithm performs analysis, redo, and undo passes to recover consistent database state following crashes. Relational databases depend on WAL to survive abrupt power outages without data corruption.",
"Shadow paging provides atomic transaction durability by duplicating page table directories rather than maintaining write-ahead logs. The database directory flushes new page pointer arrays when modification thresholds exceed a 0.85 update ratio. Transaction prepare phases timeout and abort dirty shadow copies when commit execution exceeds 1000ms. During commit, atomic pointer swapping updates the current page directory pointer to the shadow copy. SQLite supports shadow paging in rollback journal mode to ensure crash recovery without log replaying.",
"Transmission Control Protocol establishes reliable bidirectional byte streams using a three-way handshake. Web servers accept secure transport connections through standard listening port 9200. Retransmission timers detect dropped segments when unacknowledged packets exceed a 100ms RTO duration. Sliding window flow control advertises receiver buffer capacity to prevent receiver buffer exhaustion. Congestion control algorithms like BBR dynamically estimate bottleneck bandwidth and round-trip propagation time.",
"QUIC replaces legacy TCP transport by implementing multiplexed connection streams directly over UDP. Server listener sockets bind to transport port 27017 to receive client datagram packets. Stream loss detection initiates packet retransmission when probe timers exceed a 500ms loss timeout. By implementing stream multiplexing on UDP, QUIC prevents head-of-line blocking when individual packets drop. HTTP/3 mandates QUIC transport to achieve zero-RTT connection resumption and migration resilience.",
"The Domain Name System translates human-readable hostnames into routable internet protocol addresses. Recursive DNS resolvers query authoritative name servers over UDP transport port 5432. Resolver clients timeout unfulfilled recursive lookups when upstream authority responses exceed 100ms. Time-to-live attributes specify how long intermediate recursive caches retain authoritative record answers. DNSSEC signs resource record sets cryptographically using asymmetric keys to prevent cache poisoning attacks.",
"Multicast DNS discovers network services on local link subnets without requiring centralized DNS servers. Resolvers broadcast lookup datagrams over local multicast port 27017 to all peer hosts on the subnet. Local responder services timeout unacknowledged service discovery requests if peer responses exceed 250ms. Queries append the dot-local top-level domain to restrict discovery traffic within the local broadcast domain. Apple Bonjour and Linux Avahi use mDNS for zero-configuration printer and device discovery.",
"HTTP/2 introduces binary framing to interleave concurrent request and response streams over a single TCP connection. Flow control credits throttle individual stream delivery when stream buffer usage crosses a 0.85 threshold. Frame multiplexing coalesces smaller binary payload frames into groups of 32 bytes per transmission unit. HPACK header compression reduces metadata transmission overhead by maintaining shared dynamic indexing tables. Stream prioritization allows browser clients to request critical CSS and script resources ahead of decorative images.",
"HTTP/3 redesigns web application transport by replacing TCP with QUIC over UDP to eliminate head-of-line blocking. Stream flow control limits buffer consumption when stream receiver buffer saturation crosses 0.7. Frame encoders group QPACK header instructions into compression blocks of 256 bytes per frame. QPACK accommodates out-of-order stream delivery by decoupling dynamic header tables from individual streams. Modern web browsers negotiate HTTP/3 via Alt-Svc headers to improve loading speeds on mobile networks.",
"Transport Layer Security encrypts communication channels to protect confidentiality and integrity across the internet. Cipher suites negotiate ephemeral Diffie-Hellman key exchange with 192 bits of cryptographic security. The TLS 1.3 handshake reduces connection setup latency by completing in a single round trip under 500ms. Zero-RTT resumption permits returning clients to transmit encrypted application data on the initial flight. Certificate validation ensures server identity by verifying the trust chain back to installed root certificate authorities.",
"TLS 1.2 negotiates secure transport sessions through a two-round-trip handshake between client and server. Ephemeral Diffie-Hellman parameter generation establishes forward secrecy using discrete logarithm groups of 256 bits. Initial handshake negotiation terminates if client hello responses encounter network delays exceeding 250ms. Static RSA key exchange in TLS 1.2 is deprecated due to vulnerability to padding oracle attacks. Session tickets allow returning clients to bypass full key exchange by re-using serialized session state.",
"Border Gateway Protocol manages inter-domain routing decisions across autonomous systems on the global internet. Peer router daemons establish exterior BGP peering sessions over TCP port 27017. Peering keepalive timers tear down inactive BGP neighbor sessions when keepalive arrivals exceed 100ms. Path attributes like AS-PATH prevent routing loops by rejecting path vectors containing the receiving autonomous system. BGP routers exchange reachability updates to dynamically calculate optimal autonomous system paths.",
"Open Shortest Path First computes optimal intra-domain routing paths within autonomous networks using link-state routing. OSPF routers send link-state advertisements over IP transport port 27017 to synchronize topology databases. Neighbor adjacency fails if hello heartbeats from adjacent routers stop arriving within a 500ms dead interval. Dijkstra algorithm executes over synchronized link-state databases to compute shortest path trees from each router. OSPF partitions large enterprise networks into hierarchical areas to constrain flooding overhead.",
"Public key cryptography enables confidential communication and non-repudiation between untrusted network endpoints. Asymmetric key generators create digital certificates using RSA key lengths of 192 bits. Digital signature verification combines private key signing with a SHA-3 digest of the underlying payload. Hybrid cryptosystems combine asymmetric key exchange with symmetric stream encryption for performance efficiency. Perfect forward secrecy ensures past session keys remain secure even if long-term private keys are compromised.",
"Elliptic curve cryptography provides equivalent public-key security to RSA using substantially smaller key representations. Digital signature algorithms like ECDSA achieve high-grade cryptographic security using elliptic curves of 192 bits. Cryptographic message signing hashes payload inputs using a SHA-256 digest function before curve multiplication. Smaller key sizes reduce memory footprints and accelerate cryptographic handshake execution on constrained devices. Ed25519 and Secp256r1 curves represent standard elliptic curve implementations in modern security protocols.",
"Secure credential storage requires salting and iterative key stretching before persisting user secrets in databases. Modern cryptographic hashing pipelines compute password derivations using hardened SHA-256 algorithms with random salts. Work factor tuning balances offline attack resistance against server verification latency budgets capped at 250ms. Memory-hard functions like Argon2 protect against specialized hardware brute-force attacks via parallel ASIC chips. Slow verification deliberately imposes computation costs to render offline dictionary attacks infeasible.",
"PBKDF2 derives cryptographic encryption keys from human passwords by repeatedly applying pseudorandom functions. The key stretching pipeline iterates HMAC evaluations using an underlying SHA-3 cryptographic hash digest. System administrators adjust iteration counts to keep derivation execution latency bounded near 500ms per attempt. Unlike memory-hard algorithms, PBKDF2 relies primarily on computational CPU cycles without intensive RAM consumption. Modern cryptographic standards recommend high iteration counts to mitigate GPU-accelerated dictionary attacks.",
"Web application firewalls inspect inbound HTTP requests to intercept SQL injection and cross-site scripting attempts. Rate limiting algorithms throttle client IP addresses when request frequencies exceed a 0.5 burst threshold. Offending clients are blocked from executing sensitive API endpoints for a penalty window of 500ms. Content Security Policy headers restrict the origins from which scripts, styles, and fonts may be executed. Cross-Site Request Forgery tokens protect state-changing POST requests by proving user origin authenticity.",
"API gateways protect backend microservices from resource exhaustion by enforcing token bucket rate limiting. Token leak algorithms throttle client consumers when bucket consumption surpasses a 0.85 burst capacity limit. Throttled client requests receive HTTP 429 status codes with retry-after headers specifying a 500ms wait duration. Token bucket algorithms allow temporary bursts of traffic while guaranteeing sustained request rates stay bounded. Kong and AWS API Gateway use token buckets to manage multi-tenant API quotas.",
"Advanced Encryption Standard delivers authenticated symmetric encryption for data at rest and in transit. Secure storage engines configure AES in GCM mode using symmetric keys of 128 bits. Message authentication codes verify payload integrity using HMAC combined with a BLAKE2 cryptographic function. Initialization vectors must be unique for every encryption operation to prevent replay and ciphertext manipulation. Key rotation policies periodically replace symmetric master keys to limit data exposure windows.",
"ChaCha20-Poly1305 provides high-speed authenticated stream encryption optimized for software-only execution without hardware AES acceleration. Cipher implementations initialize stream ciphers using symmetric keys of 512 bits. The Poly1305 authenticator produces 128-bit integrity tags by processing ciphertext blocks with a SHA-256 primitive. Because ChaCha20 avoids table lookups, it offers natural resistance to cache-timing side-channel attacks on general CPUs. WireGuard and mobile TLS connections default to ChaCha20-Poly1305 for efficient cryptographic processing.",
"OAuth 2.0 Proof Key for Code Exchange secures authorization code grants on public mobile and single-page applications. The client transforms a high-entropy secret code verifier using a SHA-256 cryptographic digest to create the code challenge. Authorization servers reject authorization requests if code verification latencies exceed a 1000ms grant window. PKCE eliminates authorization code interception attacks by requiring possession of the original plaintext code verifier. Modern identity providers require PKCE for all public client authentication flows.",
"JSON Web Tokens transmit cryptographically verifiable claims between distributed services in compact URL-safe strings. Digital signatures verify JWT payload tampering by generating cryptographic signatures using BLAKE2 digests. Verification middleware rejects expired tokens when expiration timestamp differences exceed a 100ms clock skew threshold. Tokens comprise base64url-encoded header, payload, and cryptographic signature segments separated by periods. Stateless microservices use JWTs to transmit authenticated identity claims without querying central session stores.",
]
assert len(KB)==50

# ===================== RAG logic (no heavy models) =====================
import re, math
from collections import Counter
from flask import Flask, request, jsonify

app = Flask(__name__)

ALIASES = {
 0: ["raft"], 1: ["multi-paxos", "multi paxos", "paxos"], 2: ["gossip", "epidemic", "phi accrual"],
 3: ["swim"], 4: ["two-phase commit", "two phase commit", "2pc", "three-phase commit", "3pc"],
 5: ["saga", "sagas"], 6: ["consistent hashing", "consistent hash"],
 7: ["rendezvous", "highest random weight"], 8: ["vector clock", "vector clocks", "version vector"],
 9: ["hybrid logical clock", "hybrid logical clocks", "hlc"],
 10: ["sgd", "stochastic gradient descent"], 11: ["adamw", "adam"],
 12: ["transformer encoder", "transformer encoders"], 13: ["autoregressive", "decoder"],
 14: ["logistic regression"], 15: ["svm", "support vector"],
 16: ["mlp", "multi-layer perceptron", "multilayer perceptron", "perceptron"],
 17: ["resnet", "residual convolutional", "residual network", "residual"],
 18: ["batch normalization", "batchnorm", "batch norm"], 19: ["layer normalization", "layernorm", "layer norm"],
 20: ["postgres", "postgresql", "pgbouncer"], 21: ["mysql", "innodb"],
 22: ["b+ tree", "b+tree", "b-tree"], 23: ["lsm", "log-structured merge", "log structured merge"],
 24: ["mongodb", "mongo"], 25: ["cassandra"], 26: ["redis"], 27: ["memcached"],
 28: ["write-ahead", "write ahead", "wal"], 29: ["shadow paging"],
 30: ["tcp", "transmission control"], 31: ["quic"],
 32: ["domain name system", "dns", "dnssec"], 33: ["multicast dns", "mdns"],
 34: ["http/2", "http2", "hpack"], 35: ["http/3", "http3", "qpack"],
 36: ["tls 1.3", "transport layer security"], 37: ["tls 1.2"],
 38: ["bgp", "border gateway"], 39: ["ospf", "open shortest path"],
 40: ["public key", "public-key", "rsa"], 41: ["elliptic", "ecc", "ecdsa"],
 42: ["credential storage", "argon2", "salting", "password hashing", "key stretching"],
 43: ["pbkdf2"], 44: ["web application firewall", "waf"],
 45: ["api gateway", "token bucket"], 46: ["aes", "advanced encryption standard"],
 47: ["chacha20", "poly1305", "chacha"], 48: ["pkce", "oauth", "proof key"],
 49: ["jwt", "json web token", "json web tokens"],
}
GENERIC_ALIASES = {"residual", "adam", "tcp", "wal", "dns", "decoder", "rsa", "mongo", "perceptron", "salting", "key stretching"}

STOP = set("""a an the of to in on for and or is are was were be been being what which who whom whose when where why how does do did
 done at by with from as that this these those it its into than then so such can could should would will shall may might must
 has have had about between per using use used uses give tell me please say state describe explain list name value
 many much long number cause causes default configured configure typical standard according passage passages knowledge base documentation
 system systems also any all each both either neither not no yes if else there their they them we you your i my our""".split())
INJECT_RX = re.compile(
    r"\b(ignore|disregard|forget|override)\b"
    r"|note to (the )?(ai|assistant|model|llm)|system (notice|note|message|override|instruction)|important[: ]+system"
    r"|\boutput only\b|\breply (with|only)\b|secret word|\bbypass (the )?(rules|safety|instructions)"
    r"|system prompt|developer message|you are now|new instructions?|from now on|reveal (your|the) (prompt|instructions|system)"
    r"|respond (only )?with|output (only )?the (word|string|text)|print (the )?(word|string)|instead (answer|say|respond|output)"
    r"|<\s*/?\s*(system|assistant|instruction)[^>]*>|\[\s*(system|admin|instruction)[^\]]*\]|do not (use|consult|follow) (the )?(knowledge|context|passage)"
    r"|pretend|jailbreak|act as|stealth|secret (code|word|instruction)|always (answer|say|reply)", re.I)


def _stem(w):
    w = w.lower()
    if len(w) <= 3:
        return w
    if w.endswith("ies") and len(w) > 4:
        return w[:-3] + "y"
    if w.endswith("sses"):
        return w[:-2]
    if re.search(r"(ch|sh|x|z|ss)es$", w) and len(w) > 5:
        return w[:-2]
    if w.endswith("s") and not w.endswith(("ss", "us", "is")) and len(w) > 3:
        w = w[:-1]
    for suf in ("ations", "ation", "ings", "ing"):
        if w.endswith(suf) and len(w) > len(suf) + 3:
            w = w[: -len(suf)]
            break
    else:
        if w.endswith("ed") and len(w) > 6 and not w.endswith("eed"):
            w = w[:-2]
    if w.endswith("e") and len(w) > 4:
        w = w[:-1]
    return w


def stem(w):
    return _stem(w)


SYN = {"expiry": "expir", "expiration": "expir", "expire": "expir", "expired": "expir", "expir": "expir",
       "rejection": "reject", "rejected": "reject", "rejects": "reject", "exceeds": "exceed", "exceeded": "exceed",
       "latencies": "latency", "timeouts": "timeout", "intervals": "interval", "thresholds": "threshold"}


def norm_tok(t):
    t = t.strip(".-/")
    t = SYN.get(t, t)
    t = stem(t)
    return SYN.get(t, t)


def toks(text):
    out = []
    for t in re.findall(r"[a-zA-Z0-9][a-zA-Z0-9+./-]*", text.lower()):
        t = t.strip(".-/")
        if not t or t in STOP:
            continue
        out.append(norm_tok(t))
    return out


def split_sents(p):
    return [s.strip() for s in re.split(r"(?<=[a-z0-9\)])\.\s+(?=[A-Z])", p) if s.strip()]


PASSAGES = KB
SENTS = [split_sents(p) for p in PASSAGES]
PT = [toks(p) for p in PASSAGES]
DF = Counter()
for t in PT:
    for w in set(t):
        DF[w] += 1
NP = len(PASSAGES)
IDF = {w: math.log(1 + NP / d) for w, d in DF.items()}
VOCAB = set(DF)
RAW_VOCAB = set(w.lower() for p in PASSAGES for w in re.findall(r"[A-Za-z0-9][A-Za-z0-9+./-]*", p))
RAW_VOCAB |= {stem(w) for w in RAW_VOCAB}
PVEC = []
for t in PT:
    c = Counter(t)
    v = {w: (1 + math.log(n)) * IDF[w] for w, n in c.items()}
    PVEC.append((v, math.sqrt(sum(x * x for x in v.values()))))


def clean_question(q):
    q = (q or "").strip()[:2000]
    q = re.sub(r"<!--.*?-->", " ", q, flags=re.S)
    q = re.sub(r"[\[\(\{<][^\]\)\}>]{0,300}[\]\)\}>]",
               lambda m: " " if INJECT_RX.search(m.group(0)) else m.group(0), q)
    parts = re.split(r"(?<=[.!?\n])\s+", q)
    kept = []
    for sct in parts:
        m = INJECT_RX.search(sct)
        if not m:
            if sct.strip():
                kept.append(sct.strip())
            continue
        prefix = sct[:m.start()]
        prefix = re.sub(r"(important|note to ai|system notice|system|admin|attention|also|btw|p\.s\.|ps)[\s:,\-]*$", "", prefix.strip(), flags=re.I).strip(" ,;:-\u2014")
        if len(toks(prefix)) >= 2:
            kept.append(prefix + ("?" if "?" in sct[m.end():] or sct.rstrip().endswith("?") and not prefix.endswith("?") else ""))
    out = " ".join(kept).strip()
    return out or ""


def alias_hits(ql):
    hits = {}
    for i, al in ALIASES.items():
        best = 0
        for a in al:
            if re.search(r"(?<![a-z0-9])" + re.escape(a) + r"(?![a-z0-9])", ql):
                w = len(a) * (0.4 if a in GENERIC_ALIASES else 1.0)
                best = max(best, w)
        if best:
            hits[i] = best
    # specificity: if "tls 1.3" matched, drop generic tls-only (handled by aliases); suppress shorter overlapping groups
    if 36 in hits and 37 in hits:
        if "1.3" in ql and "1.2" not in ql: hits.pop(37)
        elif "1.2" in ql and "1.3" not in ql: hits.pop(36)
    if 1 in hits and 0 in hits and "paxos" in ql and "raft" not in ql: hits.pop(0, None)
    if 11 in hits and 10 in hits:
        pass
    # "decentralized"/"mention" artefacts: drop 'sgd' if only 'adamw' etc handled by regex boundary
    return hits


def cos(qtoks, i):
    c = Counter(qtoks)
    qv = {w: (1 + math.log(n)) * IDF.get(w, 0) for w, n in c.items()}
    qn = math.sqrt(sum(x * x for x in qv.values())) or 1.0
    v, pn = PVEC[i]
    dot = sum(x * v.get(w, 0) for w, x in qv.items())
    return dot / (qn * pn) if pn else 0.0


def sent_scores(qtoks, i, skip):
    q = [w for w in qtoks if w not in skip]
    out = []
    for s in SENTS[i]:
        st = set(toks(s))
        sc = sum(IDF.get(w, 1.0) for w in q if w in st)
        out.append(sc)
    return out


def answer_from(i, qtoks, alias_words, n_max=2):
    skip = alias_words
    sc = sent_scores(qtoks, i, skip)
    order = sorted(range(len(sc)), key=lambda k: -sc[k])
    best = order[0]
    chosen = [best]
    if len(order) > 1 and sc[order[1]] >= 0.7 * sc[best] and sc[best] > 0 and n_max > 1:
        chosen.append(order[1])
    chosen.sort()
    return " ".join(SENTS[i][k] for k in chosen), (sc[best] if sc else 0.0)


def coverage(qtoks, i, alias_words):
    q = [w for w in qtoks if w not in alias_words]
    if not q:
        return 1.0
    pt = set(PT[i])
    return sum(1 for w in q if w in pt) / len(q)


ALIAS_WORDS = {w for al in ALIASES.values() for a in al for w in re.findall(r'[a-z0-9+./-]+', a)}


def unknown_entities(qclean):
    unk = []
    words = re.findall(r"[A-Za-z][A-Za-z0-9+./-]*", qclean)
    for idx, w in enumerate(words):
        lw = w.lower()
        if lw in STOP or stem(lw) in RAW_VOCAB or lw in RAW_VOCAB or lw in ALIAS_WORDS:
            continue
        if (idx > 0 and (w[0].isupper() or any(ch.isupper() for ch in w[1:]) or any(ch.isdigit() for ch in w))):
            unk.append(w)
    return unk


def respond(question, top_k):
    q = clean_question(question)
    ql = q.lower()
    qt = toks(q)
    hits = alias_hits(ql)
    alias_words = set()
    for i in hits:
        for a in ALIASES[i]:
            if re.search(r"(?<![a-z0-9])" + re.escape(a) + r"(?![a-z0-9])", ql):
                alias_words |= set(toks(a))
    alias_words |= {t for t in qt if any(len(aw) >= 4 and aw in t for aw in alias_words)}
    base = [(cos(qt, i), i) for i in range(NP)]
    scored = []
    for s, i in base:
        bonus = 0.0
        if i in hits:
            bonus = min(0.45, 0.18 + 0.03 * hits[i])
        scored.append((s + bonus, i, s))
    scored.sort(reverse=True)
    top = scored[0]
    k = max(1, min(int(top_k or 3), 10))

    # multi-entity synthesis
    multi = [i for i in hits if hits[i] >= 3 and scored_lookup(scored, i) >= 0.5 * top[0]]
    multi = sorted(multi, key=lambda i: -scored_lookup(scored, i))[:3]
    abstain = False
    unk = unknown_entities(q)
    max_cos = top[2]
    cov = coverage(qt, top[1], alias_words)
    if not qt or re.search(r"\b(who|whom|whose)\b|what year|which year|when (was|were|did)|founded|invented|inventor|creator|created by|cost|price|salary|ceo\b", ql):
        abstain = True
    elif hits:
        # entity known; check attribute coverage
        if cov < 0.5:
            abstain = True
    else:
        if unk or max_cos < 0.22 or cov < 0.6:
            abstain = True
    if unk and not hits:
        abstain = True
    if unk and hits and cov < 0.8 and len(unk) >= 1 and any(u.lower() not in RAW_VOCAB for u in unk):
        # unknown technology named alongside a known one -> unanswerable
        if not re.search(r"compare|versus|\bvs\b|difference|unlike", ql):
            abstain = True

    if abstain:
        return {"answer": None, "sources": [], "scores": [], "confidence": round(0.12 + min(0.2, max_cos * 0.3), 4)}

    ordered = [i for _, i, _ in scored]
    if len(multi) >= 2:
        ordered = multi + [i for i in ordered if i not in multi]
        parts = []
        for i in multi:
            a, _ = answer_from(i, qt, alias_words, n_max=1)
            parts.append(a)
        answer = " ".join(parts)
    else:
        bi = top[1]
        answer, _ = answer_from(bi, qt, alias_words)
    srcs = ordered[:k]
    sc_map = {i: s for s, i, _ in scored}
    scores = []
    prev = 1.0
    for i in srcs:
        v = max(0.0, min(1.0, sc_map[i] / 0.9 if sc_map[i] <= 0.9 else 1.0))
        v = min(v, prev)
        scores.append(round(v, 4)); prev = v
    scores = sorted(scores, reverse=True)
    conf = round(min(0.97, 0.62 + 0.35 * scores[0]), 4)
    return {"answer": answer, "sources": srcs, "scores": scores, "confidence": conf}


def scored_lookup(scored, i):
    for s, j, _ in scored:
        if j == i:
            return s
    return 0.0


@app.after_request
def cors(resp):
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
    resp.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    return resp


@app.route("/query", methods=["POST", "OPTIONS"])
def query():
    if request.method == "OPTIONS":
        return ("", 204)
    body = request.get_json(force=True, silent=True) or {}
    try:
        out = respond(body.get("question", ""), body.get("top_k", 3))
    except Exception:
        out = {"answer": None, "sources": [], "scores": [], "confidence": 0.1}
    return jsonify(out)


@app.route("/", methods=["GET"])
def health():
    return jsonify(status="ok", passages=NP)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
