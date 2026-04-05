SYLLABUS = {
    "DBMS": {
        "weight": 22,
        "topics": {
            "SQL": ["SELECT", "JOIN", "GROUP BY", "HAVING", "ORDER BY", "Subqueries", "Aggregate Functions"],
            "Normalization": ["1NF", "2NF", "3NF", "BCNF", "Functional Dependencies"],
            "Keys": ["Primary", "Foreign", "Candidate", "Super", "Composite"],
            "Transactions": ["ACID", "2-Phase Locking", "Serializability", "Isolation Levels"],
            "ER Model": ["Entity Types", "Relationships", "ER to Relational Schema"],
            "Relational Algebra": ["Select (σ)", "Project (π)", "Union", "Join (⋈)", "Difference"]
        }
    },
    "CN": {
        "weight": 20,
        "topics": {
            "OSI Model": ["7 Layers", "Layer Functions", "Layer Protocols", "PDU Names"],
            "TCP/IP": ["TCP vs UDP", "3-Way Handshake", "Port Numbers", "Flow Control"],
            "IP Addressing": ["IPv4 Classes", "Subnetting", "CIDR", "Private Ranges", "IPv6 Basics"],
            "Protocols": ["HTTP/HTTPS", "FTP", "DNS", "SMTP", "DHCP", "ARP", "RARP"],
            "Routing": ["RIP", "OSPF", "BGP", "Static vs Dynamic"],
            "Devices": ["Hub vs Switch vs Router", "MAC Address", "ARP Resolution"]
        }
    },
    "OS": {
        "weight": 18,
        "topics": {
            "CPU Scheduling": ["FCFS", "SJF", "SRTF", "Round Robin", "Priority", "Avg WT/TAT Numericals"],
            "Deadlock": ["4 Conditions", "Prevention", "Avoidance", "Banker's Algorithm", "Detection"],
            "Memory Management": ["Paging", "Segmentation", "Page Replacement (FIFO/LRU/Optimal)", "Virtual Memory"],
            "Process Management": ["Process States", "PCB", "Process vs Thread", "Context Switching"],
            "Synchronization": ["Critical Section", "Semaphore", "Mutex", "Producer-Consumer"],
            "File Systems": ["Allocation Methods", "Disk Scheduling (SSTF/SCAN)", "Inode"]
        }
    },
    "DSA": {
        "weight": 15,
        "topics": {
            "Complexity": ["Big-O Notation", "Time Complexity", "Space Complexity", "Best/Avg/Worst Case"],
            "Trees": ["BST", "AVL Tree", "Heap (Min/Max)", "Traversals", "B-Tree"],
            "Sorting": ["Bubble", "Insertion", "Selection", "Merge", "Quick", "Heap Sort", "Stability"],
            "Linear Structures": ["Array", "Linked List", "Stack (LIFO)", "Queue (FIFO)", "Deque"],
            "Graph Algorithms": ["BFS", "DFS", "Dijkstra", "Bellman-Ford", "Kruskal", "Prim", "Topological Sort"],
            "Hashing": ["Hash Functions", "Collision Resolution", "Chaining", "Open Addressing", "Load Factor"]
        }
    },
    "SE": {
        "weight": 10,
        "topics": {
            "SDLC Models": ["Waterfall", "V-Model", "Spiral", "Agile", "RAD", "Iterative"],
            "Testing": ["Black Box", "White Box", "Unit", "Integration", "System", "Regression", "Alpha/Beta"],
            "Metrics": ["Cyclomatic Complexity", "Function Points", "Cohesion", "Coupling"],
            "Design": ["Design Patterns", "Creational", "Structural", "Behavioral"]
        }
    },
    "OOP": {
        "weight": 8,
        "topics": {
            "4 Pillars": ["Encapsulation", "Inheritance", "Polymorphism", "Abstraction"],
            "Key Concepts": ["Overloading vs Overriding", "Abstract Class vs Interface", "Multiple Inheritance"],
            "Java Specifics": ["Constructor Rules", "Static vs Instance", "final/abstract keywords"]
        }
    },
    "WEB_TECH": {
        "weight": 4,
        "topics": {
            "HTTP": ["GET/POST/PUT/DELETE", "Status Codes", "Stateless Protocol", "Cookies vs Sessions"],
            "Architecture": ["REST vs SOAP", "JSON vs XML", "Client-Server Model"]
        }
    },
    "CYBERSECURITY": {
        "weight": 4,
        "topics": {
            "Cryptography": ["Symmetric (AES/DES)", "Asymmetric (RSA)", "Hashing (MD5/SHA)", "SSL/TLS"],
            "Threats": ["SQL Injection", "XSS", "MITM", "DDoS", "Phishing", "Ransomware"],
            "Defense": ["Firewall Types", "VPN", "IDS/IPS", "PKI"]
        }
    },
    "CLOUD": {
        "weight": 3,
        "topics": {
            "Service Models": ["IaaS", "PaaS", "SaaS"],
            "Deployment": ["Public", "Private", "Hybrid", "Community"],
            "Virtualization": ["Hypervisor Type 1", "Hypervisor Type 2", "Containers vs VMs"]
        }
    },

    # ── NEW SECTIONS ──────────────────────────────────────────────────────────

    "AI": {
        "weight": 6,
        "exam_note": "Appearing in IBPS SO IT papers since 2022; expect 3-5 conceptual questions",
        "topics": {
            "Foundations": [
                "AI vs ML vs DL hierarchy",
                "Turing Test",
                "Strong AI vs Weak AI",
                "Knowledge Representation",
                "Intelligent Agents (PEAS)"
            ],
            "Search Algorithms": [
                "BFS / DFS (uninformed)",
                "A* Search (informed)",
                "Heuristic Functions",
                "Hill Climbing",
                "Minimax Algorithm",
                "Alpha-Beta Pruning"
            ],
            "Knowledge & Reasoning": [
                "Propositional Logic",
                "First-Order Logic (FOL)",
                "Inference Rules",
                "Forward vs Backward Chaining",
                "Expert Systems",
                "Fuzzy Logic"
            ],
            "Planning & Agents": [
                "STRIPS Planning",
                "Reactive vs Deliberative Agents",
                "Multi-Agent Systems",
                "Reflex vs Goal-based Agents"
            ],
            "NLP Basics": [
                "Tokenization",
                "Stemming vs Lemmatization",
                "POS Tagging",
                "Named Entity Recognition (NER)",
                "Bag of Words",
                "TF-IDF"
            ]
        }
    },

    "ML": {
        "weight": 7,
        "exam_note": "Weightage increasing each year; focus on algorithms, terminology, and evaluation metrics",
        "topics": {
            "Core Concepts": [
                "Supervised vs Unsupervised vs Reinforcement Learning",
                "Training / Validation / Test Split",
                "Overfitting vs Underfitting",
                "Bias-Variance Tradeoff",
                "Cross-Validation (k-Fold)",
                "Feature Engineering & Selection"
            ],
            "Supervised Algorithms": [
                "Linear Regression (MSE, Gradient Descent)",
                "Logistic Regression (Sigmoid, Binary Classification)",
                "Decision Tree (Gini, Entropy, Information Gain)",
                "Random Forest (Bagging, Ensemble)",
                "SVM (Hyperplane, Kernel Trick, Margin)",
                "KNN (Distance Metrics, k selection)",
                "Naive Bayes (Bayes Theorem, Conditional Probability)"
            ],
            "Unsupervised Algorithms": [
                "K-Means Clustering (Elbow Method)",
                "Hierarchical Clustering (Dendrogram)",
                "DBSCAN",
                "PCA (Dimensionality Reduction, Eigenvalues)",
                "Autoencoders (basics)"
            ],
            "Evaluation Metrics": [
                "Confusion Matrix (TP/TN/FP/FN)",
                "Accuracy / Precision / Recall / F1-Score",
                "ROC Curve & AUC",
                "RMSE / MAE (Regression)",
                "Silhouette Score (Clustering)"
            ],
            "Regularization & Optimization": [
                "L1 Regularization (Lasso)",
                "L2 Regularization (Ridge)",
                "Elastic Net",
                "Gradient Descent variants (SGD, Mini-batch, Adam)"
            ]
        }
    },

    "DEEP_LEARNING": {
        "weight": 5,
        "exam_note": "Conceptual questions only — no backprop math; focus on architecture names and use cases",
        "topics": {
            "Neural Network Basics": [
                "Perceptron",
                "Multilayer Perceptron (MLP)",
                "Activation Functions (ReLU, Sigmoid, Tanh, Softmax)",
                "Forward Propagation",
                "Backpropagation & Chain Rule",
                "Vanishing / Exploding Gradient"
            ],
            "CNN": [
                "Convolution Layer",
                "Pooling (Max/Avg)",
                "Feature Maps",
                "Fully Connected Layer",
                "Use case: Image Classification",
                "Famous architectures: LeNet, VGG, ResNet"
            ],
            "RNN & Variants": [
                "Recurrent Neural Network",
                "Vanishing Gradient in RNN",
                "LSTM (Long Short-Term Memory)",
                "GRU (Gated Recurrent Unit)",
                "Use case: Sequence / Time-series / NLP"
            ],
            "Transformers & LLMs": [
                "Attention Mechanism",
                "Self-Attention",
                "BERT (Bidirectional, Masked LM)",
                "GPT (Autoregressive, Generative)",
                "Transformer architecture (Encoder-Decoder)",
                "Tokenization (BPE, WordPiece)",
                "Prompt Engineering basics",
                "Fine-tuning vs RAG"
            ],
            "Generative Models": [
                "GAN (Generator vs Discriminator)",
                "VAE (Variational Autoencoder)",
                "Diffusion Models (concept)",
                "Use cases: Image synthesis, Deepfakes"
            ]
        }
    },

    "DATA_SCIENCE": {
        "weight": 4,
        "exam_note": "Overlaps with ML; focus on pipeline steps and statistical concepts",
        "topics": {
            "Statistics Basics": [
                "Mean / Median / Mode",
                "Variance & Standard Deviation",
                "Normal Distribution",
                "Skewness & Kurtosis",
                "Correlation vs Causation",
                "Pearson vs Spearman Correlation"
            ],
            "Probability": [
                "Bayes Theorem",
                "Conditional Probability",
                "Probability Distributions (Binomial, Poisson, Gaussian)",
                "Hypothesis Testing (p-value, t-test, chi-square)"
            ],
            "Data Pipeline": [
                "Data Collection → Cleaning → EDA → Modeling → Deployment",
                "Handling Missing Values (imputation, dropping)",
                "Outlier Detection (IQR, Z-score)",
                "Data Normalization vs Standardization",
                "One-Hot Encoding vs Label Encoding"
            ],
            "Big Data": [
                "Hadoop (HDFS, MapReduce)",
                "Spark (RDD, DataFrame, lazy evaluation)",
                "Batch vs Stream Processing",
                "Kafka (message queue basics)",
                "Data Warehouse vs Data Lake",
                "OLAP vs OLTP"
            ],
            "Visualization": [
                "Matplotlib / Seaborn (concept level)",
                "Dashboard tools: Tableau, Power BI",
                "Chart selection: when to use what"
            ]
        }
    },

    "TRENDING_TECH": {
        "weight": 4,
        "exam_note": "1-3 awareness questions per paper; definitions and use cases are enough",
        "topics": {
            "Blockchain": [
                "Distributed Ledger Technology (DLT)",
                "Block structure (Hash, Nonce, Merkle Tree)",
                "Consensus Mechanisms (PoW, PoS, DPoS)",
                "Smart Contracts",
                "Public vs Private vs Consortium Blockchain",
                "Cryptocurrency basics (Bitcoin, Ethereum)",
                "NFT concept"
            ],
            "IoT": [
                "IoT Architecture (Perception → Network → Application)",
                "IoT Protocols (MQTT, CoAP, Zigbee)",
                "Edge Computing vs Fog Computing",
                "IoT Security challenges",
                "Smart devices, RFID, Sensors"
            ],
            "DevOps & Containers": [
                "CI/CD Pipeline",
                "Docker (Image, Container, Dockerfile)",
                "Kubernetes (Pod, Node, Cluster, Orchestration)",
                "Microservices vs Monolithic",
                "Git (version control, branching strategies)",
                "Jenkins, GitHub Actions (concept)"
            ],
            "AR / VR / Metaverse": [
                "Augmented Reality vs Virtual Reality vs Mixed Reality",
                "XR (Extended Reality)",
                "Metaverse concept",
                "Use cases in banking: virtual branches, AR KYC"
            ],
            "Quantum Computing": [
                "Qubit vs Classical Bit",
                "Superposition & Entanglement",
                "Quantum Gates (Hadamard, CNOT)",
                "Quantum Supremacy",
                "Threat to RSA encryption (Shor's algorithm concept)",
                "Post-Quantum Cryptography"
            ],
            "Fintech & Banking Tech": [
                "UPI architecture",
                "CBDC (Central Bank Digital Currency)",
                "Open Banking & APIs",
                "RegTech / SupTech",
                "Robo-advisors",
                "Digital Lending & BNPL",
                "AI in fraud detection"
            ]
        }
    }
}

# ── Quick-access helpers ───────────────────────────────────────────────────────

PRIORITY_ORDER = sorted(
    SYLLABUS.items(),
    key=lambda x: x[1]["weight"],
    reverse=True
)

TOTAL_TOPICS = sum(
    len(sub_topics)
    for subject in SYLLABUS.values()
    for sub_topics in subject["topics"].values()
)

SUBJECT_SUMMARY = {
    subject: {
        "weight": data["weight"],
        "num_chapters": len(data["topics"]),
        "num_subtopics": sum(len(v) for v in data["topics"].values()),
        "exam_note": data.get("exam_note", "Core subject — standard weightage")
    }
    for subject, data in SYLLABUS.items()
}