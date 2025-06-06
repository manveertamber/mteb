from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskSTS import AbsTaskSTS


class STS15STS(AbsTaskSTS):
    metadata = TaskMetadata(
        name="STS15",
        dataset={
            "path": "mteb/sts15-sts",
            "revision": "ae752c7c21bf194d8b67fd573edf7ae58183cbe3",
        },
        description="SemEval STS 2015 dataset",
        reference="https://www.aclweb.org/anthology/S15-2010",
        type="STS",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="cosine_spearman",
        date=("2008-01-01", "2014-07-28"),
        domains=["Blog", "News", "Web", "Written", "Spoken"],
        task_subtypes=[],
        license="not specified",
        annotations_creators="human-annotated",
        dialect=[],
        sample_creation="created",
        bibtex_citation=r"""
@inproceedings{bicici-2015-rtm,
  address = {Denver, Colorado},
  author = {Bi{\c{c}}ici, Ergun},
  booktitle = {Proceedings of the 9th International Workshop on Semantic Evaluation ({S}em{E}val 2015)},
  doi = {10.18653/v1/S15-2010},
  editor = {Nakov, Preslav  and
Zesch, Torsten  and
Cer, Daniel  and
Jurgens, David},
  month = jun,
  pages = {56--63},
  publisher = {Association for Computational Linguistics},
  title = {{RTM}-{DCU}: Predicting Semantic Similarity with Referential Translation Machines},
  url = {https://aclanthology.org/S15-2010},
  year = {2015},
}
""",
    )

    @property
    def metadata_dict(self) -> dict[str, str]:
        metadata_dict = super().metadata_dict
        metadata_dict["min_score"] = 0
        metadata_dict["max_score"] = 5
        return metadata_dict
