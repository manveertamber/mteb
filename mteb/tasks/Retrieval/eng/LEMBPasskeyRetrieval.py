from __future__ import annotations

import datasets

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class LEMBPasskeyRetrieval(AbsTaskRetrieval):
    _EVAL_SPLIT = [
        "test_256",
        "test_512",
        "test_1024",
        "test_2048",
        "test_4096",
        "test_8192",
        "test_16384",
        "test_32768",
    ]

    metadata = TaskMetadata(
        name="LEMBPasskeyRetrieval",
        dataset={
            "path": "dwzhu/LongEmbed",
            "revision": "6e346642246bfb4928c560ee08640dc84d074e8c",
            "name": "passkey",
        },
        reference="https://huggingface.co/datasets/dwzhu/LongEmbed",
        description=("passkey subset of dwzhu/LongEmbed dataset."),
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=_EVAL_SPLIT,
        eval_langs=["eng-Latn"],
        main_score="ndcg_at_1",
        date=("2000-01-01", "2023-12-31"),
        domains=["Fiction", "Written"],
        task_subtypes=["Article retrieval"],
        license="not specified",
        annotations_creators="derived",
        dialect=[],
        sample_creation="found",
        bibtex_citation=r"""
@article{zhu2024longembed,
  author = {Zhu, Dawei and Wang, Liang and Yang, Nan and Song, Yifan and Wu, Wenhao and Wei, Furu and Li, Sujian},
  journal = {arXiv preprint arXiv:2404.12096},
  title = {LongEmbed: Extending Embedding Models for Long Context Retrieval},
  year = {2024},
}
""",
    )

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus = {}
        self.queries = {}
        self.relevant_docs = {}

        for split in self._EVAL_SPLIT:
            context_length = int(split.split("_")[1])
            query_list = datasets.load_dataset(**self.metadata_dict["dataset"])[
                "queries"
            ]  # dict_keys(['qid', 'text'])
            query_list = query_list.filter(
                lambda x: x["context_length"] == context_length
            )
            queries = {row["qid"]: row["text"] for row in query_list}

            corpus_list = datasets.load_dataset(**self.metadata_dict["dataset"])[
                "corpus"
            ]  # dict_keys(['doc_id', 'text'])
            corpus_list = corpus_list.filter(
                lambda x: x["context_length"] == context_length
            )
            corpus = {row["doc_id"]: {"text": row["text"]} for row in corpus_list}

            qrels_list = datasets.load_dataset(**self.metadata_dict["dataset"])[
                "qrels"
            ]  # dict_keys(['qid', 'doc_id'])
            qrels_list = qrels_list.filter(
                lambda x: x["context_length"] == context_length
            )
            qrels = {row["qid"]: {row["doc_id"]: 1} for row in qrels_list}

            self.corpus[split] = corpus
            self.queries[split] = queries
            self.relevant_docs[split] = qrels

        self.data_loaded = True
