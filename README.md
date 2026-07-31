# Bala-ERA-V5
# Executive Summary

The quality of a foundation model depends more on the quality and composition of its training data than on the model architecture itself. Every percentage allocated to a capability consumes compute, storage, and training budget, making the mixture design an engineering decision rather than an arbitrary choice.

This document proposes a defendable mixture-and-curriculum strategy for ERA V5. Every capability lane is assigned a justified share of the training budget, mapped to real datasets, protected by minimum allocation thresholds where necessary, and validated through proxy experiments before being accepted for full-scale training.

The proposed design follows one guiding principle:

> **Every data decision is a hypothesis until validated by experiment.**

---

# 1. Engineering Objectives

ERA V5 is designed to be an India-first foundation model while remaining globally competitive.

The objectives are:

- Excellent multilingual capability with emphasis on Indian languages.
- Strong reasoning and mathematical ability.
- Competitive coding performance.
- Native support for long-context understanding.
- Agentic capability through tool usage and planning.
- High factual accuracy using trusted Indian institutional data.
- Efficient utilization of compute through high-quality data rather than excessive data volume.

---

# 2. Capability Mixture

The pretraining budget is divided across capability lanes as follows.

| Capability | Share | Engineering Justification |
|------------|-------|---------------------------|
| General Knowledge (English) | **23%** | Provides broad world knowledge and language fluency without dominating the mixture. |
| Programming & Code | **18%** | Strong coding capability is essential for software engineering, agentic workflows and execution-based reasoning. |
| Indic Languages | **18%** | Higher than global multilingual models to satisfy the India-first objective while avoiding excessive reduction in English capability. |
| Reasoning & Mathematics | **12%** | Multi-step reasoning, mathematics and logical inference require dedicated exposure beyond general web text. |
| Agentic Data | **8%** | Planning, tool usage, browser interaction and workflow execution require dedicated datasets and cannot emerge reliably from web text alone. |
| Long Context | **7%** | Enables processing of books, legal documents, research papers and long conversations. |
| India-specific Structured Knowledge | **7%** | Government, judiciary, education, finance and policy documents improve practical usefulness within India. |
| Books & Long-form Literature | **5%** | Improves coherence, narrative quality and factual consistency across long outputs. |
| Dialogue & Conversation | **2%** | Natural conversational behaviour and instruction following. |

**Total = 100%**

### Why these percentages?

The proposed mixture balances four competing objectives:

- India-first capability
- Strong reasoning
- Competitive coding performance
- Efficient use of limited compute

Increasing any single capability significantly beyond these values would necessarily reduce another capability due to a fixed training budget.

---

# 3. Indic Data Composition

The Indic allocation (18%) is further divided according to data quality.

| Data Tier | Share | Rationale |
|-----------|-------|-----------|
| Verified | **45%** | Highest trust sources providing factual and institutional knowledge. |
| Unverified | **25%** | Large-scale web knowledge that increases language diversity. |
| Translated | **20%** | Expands coverage for low-resource languages using high-quality English corpora. |
| Synthetic | **10%** | Fills capability gaps where real data is unavailable while limiting error propagation. |

## Verified Sources

- NCERT
- RBI publications
- Supreme Court Judgements
- Parliament Proceedings
- Election Commission
- ISRO publications
- Government reports
- AI4Bharat curated datasets
- High-quality Wikipedia

## Unverified Sources

- Blogs
- News archives
- Community discussions
- Public forums
- Educational websites

## Translated Sources

- Mathematics
- Science
- Programming
- Legal knowledge
- Government documentation

## Synthetic Sources

Generated using frontier LLMs with human verification where required.

Examples include:

- Question-answer pairs
- Tool-use trajectories
- Reasoning examples
- Programming problems
- Low-resource language augmentation

Synthetic data is intentionally limited to 10% to prevent amplification of model-generated errors.

---

# 4. Capability Supply Analysis

A capability cannot receive a large budget unless sufficient high-quality data exists.

| Capability | Data Availability | Gap | Strategy |
|------------|------------------|-----|----------|
| General Knowledge | High | None | Direct usage after cleaning |
| Programming | High | Small | Deduplication and execution verification |
| Indic Languages | Medium | Moderate | Translation + curated collection |
| Reasoning | Medium | Moderate | Synthetic reasoning generation |
| Agentic | Low | Large | Tool trajectories and synthetic interaction data |
| Long Context | High | None | Books, legal documents, research papers |
| India Structured Data | Medium | Small | Government publications and institutional reports |

This prevents unrealistic allocation of training budget to capability lanes that lack sufficient real-world data.

---

# 5. Dataset Mapping

Each capability lane is explicitly tied to representative datasets.

| Capability | Representative Datasets |
|------------|------------------------|
| General Knowledge | FineWeb, RefinedWeb, C4 |
| Programming | GitHub (permissive), The Stack, StarCoder |
| Reasoning | GSM8K, MATH, Proof datasets |
| Agentic | ToolBench, AgentInstruct, Browser Interaction datasets |
| Long Context | Books, Research Papers, Legal Documents |
| Indic | AI4Bharat, Sangraha, IndicCorp, Samanantar |
| India Structured | RBI, NCERT, Parliament, Supreme Court, Government reports |

---

# 6. Protected Floors

Dynamic sampling naturally favours abundant datasets.

To preserve strategic capabilities, the sampler is not permitted to reduce these lanes below the following minimum allocation.

| Capability | Protected Floor |
|------------|----------------|
| Indic Languages | 15% |
| Programming | 15% |
| Reasoning | 10% |
| Long Context | 5% |

These minimum allocations remain active throughout training.

---

# 7. Annealing Reserve

A dedicated **5% reserve** is held back for the final stages of training.

The reserve consists only of:

- Verified institutional data
- Human-reviewed instruction data
- Execution-verified code
- High-quality reasoning datasets
- High-quality multilingual conversations

### Justification

The final training stages have disproportionate impact on factual consistency and instruction following. Reserving a small percentage of the budget allows the model to consolidate knowledge without excessive exposure to noisy data.

---

# 8. Curriculum Strategy

Training progresses from simple to increasingly difficult examples.

## Phase 1 – Foundation

Objectives

- Learn language
- Learn grammar
- Learn vocabulary

Primary Data

- Books
- Wikipedia
- Filtered web

Difficulty

Mostly Level 1–2 examples.

---

## Phase 2 – Knowledge Expansion

Objectives

- Acquire domain knowledge
- Learn Indian institutions
- Learn programming syntax

Primary Data

- Programming
- Science
- Government documents
- Mathematics

Difficulty

Level 2–3.

---

## Phase 3 – Advanced Capability

Objectives

- Multi-step reasoning
- Tool use
- Agentic planning
- Long-context understanding

Primary Data

- Reasoning datasets
- Tool trajectories
- Browser interaction
- Long documents

Difficulty

Level 3–5.

---

## Phase 4 – Annealing

Objectives

- Reduce hallucinations
- Improve factual accuracy
- Improve instruction following

Primary Data

Only highest-quality verified datasets.

---

# 9. Difficulty Bands

Training samples are categorized by reasoning complexity.

| Level | Example |
|--------|----------|
| Level 1 | "What is GST?" |
| Level 2 | "Compare GST and VAT." |
| Level 3 | "Calculate GST for a transaction." |
| Level 4 | "Explain the economic impact of GST." |
| Level 5 | "Design a GST advisory system for SMEs." |

The curriculum gradually increases exposure to higher-complexity examples.

---

# 10. Reasoning Length Bands

The model is trained on reasoning chains of different lengths.

| Band | Target Length | Example |
|------|---------------|----------|
| Short | <50 tokens | Fact lookup |
| Medium | 50–200 tokens | Explanation |
| Long | 200–1000 tokens | Multi-step reasoning |
| Extended | >1000 tokens | Research report or legal analysis |

Training gradually shifts toward longer reasoning chains.

---

# 11. Data Cleaning Strategy

Cleaning continues throughout the project rather than being a one-time activity.

The pipeline includes:

- Language identification
- Duplicate removal
- Benchmark decontamination
- Toxicity filtering
- Copyright filtering
- Personally Identifiable Information removal
- Translation quality verification
- Execution verification for code
- Human audit for synthetic datasets

Priority is given to capability lanes with the highest contamination levels.

---

# 12. Proxy Experiments

Every mixture decision is treated as a hypothesis.

Three competing mixtures will be evaluated.

### Mixture A

Current proposed allocation.

### Mixture B

Higher reasoning allocation (+3%) with reduced general web.

### Mixture C

Higher Indic allocation (+3%) with reduced programming.

Models will first be trained at **1B parameters**.

The best-performing mixture will then be validated using a **3B parameter** model.

Evaluation metrics include:

- MMLU
- GSM8K
- HumanEval
- IFEval
- IndicBench
- Long-context benchmarks

The production mixture will only be finalized after proxy validation.

---

# 13. Success Criteria

The proposed strategy is successful if it demonstrates:

- Competitive multilingual performance
- Strong coding capability
- Robust reasoning accuracy
- Effective agentic planning
- High-quality Indian language support
- Stable instruction following
- Reduced hallucination rate

---

# 14. Risks and Mitigation

| Risk | Mitigation |
|------|------------|
| Limited high-quality Indic data | Translation and curated collection |
| Agentic data scarcity | Synthetic tool trajectories |
| Synthetic hallucinations | Human verification and capped usage |
| Dataset imbalance | Dynamic sampling with protected floors |
| Benchmark contamination | Continuous decontamination |

---

# 15. Conclusion

This mixture-and-curriculum plan is designed as a testable engineering specification rather than a static data allocation document. Every capability lane is justified, mapped to real datasets, protected against underrepresentation, and validated through controlled proxy experiments before full-scale deployment.

The proposed design balances India's linguistic diversity, practical institutional knowledge, advanced reasoning, software engineering capability, and agentic behaviour while recognizing that every allocation is an engineering hypothesis that must be confirmed through evidence rather than assumption
