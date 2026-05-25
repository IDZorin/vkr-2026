(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort Document 0)
(declare-sort DocumentPart 0)
(declare-sort GbsIndex 0)
(declare-sort GbsIndexUniverse 0)
(declare-sort Url 0)

(declare-const GbsIndexSpecifiedInSection2_1 GbsIndex)
(declare-const HttpsSolactiveComDownloadsGuidelineSolactiveGBSBenchmarkSeriesPdf Url)
(declare-const Section2_1 DocumentPart)
(declare-const SolactiveGBSBenchmarkSeriesGuideline Document)
(declare-const TheGbsIndexUniverse GbsIndexUniverse)

(declare-fun gbs_index_specified_in_section (GbsIndex DocumentPart) Bool)
(declare-fun index_universe_as_defined_in_guideline (GbsIndexUniverse Document) Bool)
(declare-fun index_universe_for_gbs_index (GbsIndexUniverse GbsIndex) Bool)

(assert (! (gbs_index_specified_in_section GbsIndexSpecifiedInSection2_1 Section2_1) :named TEXT_gbs_index_specified_in_section_2_1))
(assert (! (and (index_universe_as_defined_in_guideline TheGbsIndexUniverse SolactiveGBSBenchmarkSeriesGuideline) (index_universe_for_gbs_index TheGbsIndexUniverse GbsIndexSpecifiedInSection2_1)) :named TEXT_gbs_index_universe_definition))
(check-sat)
