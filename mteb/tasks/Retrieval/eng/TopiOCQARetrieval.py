from __future__ import annotations

from datasets import load_dataset

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval

CORPUS_HF_NAME, CORPUS_HF_VERSION, CORPUS_HF_SPLIT = (
    "McGill-NLP/TopiOCQA-wiki-corpus",
    "50ae3b82713b1a935190def03ce7e7e75a318636",
    "train",
)


class TopiOCQARetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="TopiOCQA",
        dataset={
            "path": "McGill-NLP/TopiOCQA",
            "revision": "66cd1dbf5577c653ecb99b385200f08e15e12f30",
            "trust_remote_code": True,
        },
        reference="https://mcgill-nlp.github.io/topiocqa",
        description=(
            "TopiOCQA (Human-in-the-loop Attributable Generative Retrieval for Information-seeking Dataset) "
            + "is information-seeking conversational dataset with challenging topic switching phenomena. "
            + "It consists of conversation histories along with manually labelled relevant/gold passage."
        ),
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["validation"],
        eval_langs=["eng-Latn"],
        main_score="ndcg_at_10",
        date=("2021-03-01", "2021-07-31"),
        domains=["Encyclopaedic", "Written"],
        task_subtypes=["Conversational retrieval"],
        license="cc-by-nc-sa-4.0",
        annotations_creators="human-annotated",
        dialect=[],
        sample_creation="found",
        bibtex_citation=r"""
@misc{adlakha2022topiocqa,
  archiveprefix = {arXiv},
  author = {Vaibhav Adlakha and Shehzaad Dhuliawala and Kaheer Suleman and Harm de Vries and Siva Reddy},
  eprint = {2110.00768},
  primaryclass = {cs.CL},
  title = {TopiOCQA: Open-domain Conversational Question Answering with Topic Switching},
  year = {2022},
}
""",
    )

    # TODO: Will be removed if curated and added to mteb HF
    def load_data(self, **kwargs):
        if self.data_loaded:
            return
        self.corpus, self.queries, self.relevant_docs = {}, {}, {}
        dataset_path = self.metadata_dict["dataset"]["path"]
        for split in kwargs.get("eval_splits", self.metadata_dict["eval_splits"]):
            corpus, queries, qrels = self._load_data_for_split(dataset_path, split)
            self.corpus[split], self.queries[split], self.relevant_docs[split] = (
                corpus,
                queries,
                qrels,
            )

        self.data_loaded = True

    def _load_data_for_split(self, dataset_path, split):
        revision = self.metadata_dict["dataset"].get("revision", None)
        ds = load_dataset(
            dataset_path,
            split=split,
            revision=revision,
        )
        queries, corpus, qrels = {}, {}, {}
        for sample in ds:
            query_id = f"{sample['Conversation_no']}-{sample['Turn_no']}"
            query = sample["Context"] + [sample["Question"]]
            doc_id = sample["Gold_passage"]["id"]
            queries[query_id] = query
            qrels[query_id] = {doc_id: 1}

        corpus_ds = load_dataset(
            CORPUS_HF_NAME, revision=CORPUS_HF_VERSION, split=CORPUS_HF_SPLIT
        )
        for doc in corpus_ds:
            doc_id = doc["id"]
            corpus[doc_id] = {
                "title": "; ".join([doc["title"], doc["sub_title"]]),
                "text": doc["contents"],
            }

        return corpus, queries, qrels


class TopiOCQARetrievalHardNegatives(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="TopiOCQAHardNegatives",
        dataset={
            "path": "mteb/TopiOCQA_validation_top_250_only_w_correct-v2",
            "revision": "b4cc09fb8bb3a9e0ce0f94dc69c96397a2a47c18",
            "trust_remote_code": True,
        },
        reference="https://mcgill-nlp.github.io/topiocqa",
        description=(
            "TopiOCQA (Human-in-the-loop Attributable Generative Retrieval for Information-seeking Dataset) "
            + "is information-seeking conversational dataset with challenging topic switching phenomena. "
            + "It consists of conversation histories along with manually labelled relevant/gold passage. The hard negative version has been created by pooling the 250 top documents per query from BM25, e5-multilingual-large and e5-mistral-instruct."
        ),
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["validation"],
        eval_langs=["eng-Latn"],
        main_score="ndcg_at_10",
        date=("2021-03-01", "2021-07-31"),
        domains=["Encyclopaedic", "Written"],
        task_subtypes=["Conversational retrieval"],
        license="cc-by-nc-sa-4.0",
        annotations_creators="human-annotated",
        dialect=[],
        sample_creation="found",
        bibtex_citation=r"""
@misc{adlakha2022topiocqa,
  archiveprefix = {arXiv},
  author = {Vaibhav Adlakha and Shehzaad Dhuliawala and Kaheer Suleman and Harm de Vries and Siva Reddy},
  eprint = {2110.00768},
  primaryclass = {cs.CL},
  title = {TopiOCQA: Open-domain Conversational Question Answering with Topic Switching},
  year = {2022},
}
""",
        adapted_from=["TopiOCQA"],
    )
