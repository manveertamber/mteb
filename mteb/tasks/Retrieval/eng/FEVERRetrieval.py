from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class FEVER(AbsTaskRetrieval):
    ignore_identical_ids = True

    metadata = TaskMetadata(
        name="FEVER",
        dataset={
            "path": "mteb/fever",
            "revision": "bea83ef9e8fb933d90a2f1d5515737465d613e12",
        },
        description=(
            "FEVER (Fact Extraction and VERification) consists of 185,445 claims generated by altering sentences"
            + " extracted from Wikipedia and subsequently verified without knowledge of the sentence they were"
            + " derived from."
        ),
        reference="https://fever.ai/",
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="ndcg_at_10",
        date=None,
        domains=["Encyclopaedic", "Written"],
        task_subtypes=["Claim verification"],
        license="cc-by-nc-sa-3.0",
        annotations_creators="human-annotated",
        dialect=[],
        sample_creation="found",
        bibtex_citation=r"""
@inproceedings{thorne-etal-2018-fever,
  abstract = {In this paper we introduce a new publicly available dataset for verification against textual sources, FEVER: Fact Extraction and VERification. It consists of 185,445 claims generated by altering sentences extracted from Wikipedia and subsequently verified without knowledge of the sentence they were derived from. The claims are classified as Supported, Refuted or NotEnoughInfo by annotators achieving 0.6841 in Fleiss kappa. For the first two classes, the annotators also recorded the sentence(s) forming the necessary evidence for their judgment. To characterize the challenge of the dataset presented, we develop a pipeline approach and compare it to suitably designed oracles. The best accuracy we achieve on labeling a claim accompanied by the correct evidence is 31.87{\%}, while if we ignore the evidence we achieve 50.91{\%}. Thus we believe that FEVER is a challenging testbed that will help stimulate progress on claim verification against textual sources.},
  address = {New Orleans, Louisiana},
  author = {Thorne, James  and
Vlachos, Andreas  and
Christodoulopoulos, Christos  and
Mittal, Arpit},
  booktitle = {Proceedings of the 2018 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)},
  doi = {10.18653/v1/N18-1074},
  editor = {Walker, Marilyn  and
Ji, Heng  and
Stent, Amanda},
  month = jun,
  pages = {809--819},
  publisher = {Association for Computational Linguistics},
  title = {{FEVER}: a Large-scale Dataset for Fact Extraction and {VER}ification},
  url = {https://aclanthology.org/N18-1074},
  year = {2018},
}
""",
        prompt={
            "query": "Given a claim, retrieve documents that support or refute the claim"
        },
    )


class FEVERHardNegatives(AbsTaskRetrieval):
    ignore_identical_ids = True

    metadata = TaskMetadata(
        name="FEVERHardNegatives",
        dataset={
            "path": "mteb/FEVER_test_top_250_only_w_correct-v2",
            "revision": "080c9ed6267b65029207906e815d44a9240bafca",
        },
        description=(
            "FEVER (Fact Extraction and VERification) consists of 185,445 claims generated by altering sentences"
            + " extracted from Wikipedia and subsequently verified without knowledge of the sentence they were"
            + " derived from. The hard negative version has been created by pooling the 250 top documents per query from BM25, e5-multilingual-large and e5-mistral-instruct."
        ),
        reference="https://fever.ai/",
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="ndcg_at_10",
        date=None,
        domains=["Encyclopaedic", "Written"],
        task_subtypes=["Claim verification"],
        license="cc-by-nc-sa-3.0",
        annotations_creators="human-annotated",
        dialect=None,
        sample_creation=None,
        bibtex_citation=r"""
@inproceedings{thorne-etal-2018-fever,
  abstract = {In this paper we introduce a new publicly available dataset for verification against textual sources, FEVER: Fact Extraction and VERification. It consists of 185,445 claims generated by altering sentences extracted from Wikipedia and subsequently verified without knowledge of the sentence they were derived from. The claims are classified as Supported, Refuted or NotEnoughInfo by annotators achieving 0.6841 in Fleiss kappa. For the first two classes, the annotators also recorded the sentence(s) forming the necessary evidence for their judgment. To characterize the challenge of the dataset presented, we develop a pipeline approach and compare it to suitably designed oracles. The best accuracy we achieve on labeling a claim accompanied by the correct evidence is 31.87{\%}, while if we ignore the evidence we achieve 50.91{\%}. Thus we believe that FEVER is a challenging testbed that will help stimulate progress on claim verification against textual sources.},
  address = {New Orleans, Louisiana},
  author = {Thorne, James  and
Vlachos, Andreas  and
Christodoulopoulos, Christos  and
Mittal, Arpit},
  booktitle = {Proceedings of the 2018 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)},
  doi = {10.18653/v1/N18-1074},
  editor = {Walker, Marilyn  and
Ji, Heng  and
Stent, Amanda},
  month = jun,
  pages = {809--819},
  publisher = {Association for Computational Linguistics},
  title = {{FEVER}: a Large-scale Dataset for Fact Extraction and {VER}ification},
  url = {https://aclanthology.org/N18-1074},
  year = {2018},
}
""",
        adapted_from=["FEVER"],
    )
