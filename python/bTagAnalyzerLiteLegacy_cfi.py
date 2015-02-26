import FWCore.ParameterSet.Config as cms

from RecoBTag.BTagAnalyzerLite.bTagAnalyzerLiteCommon_cff import *

bTagAnalyzerLiteLegacy = cms.EDAnalyzer("BTagAnalyzerLiteLegacy",
    bTagAnalyzerLiteCommon,
    # computers
    svComputer        = cms.string('combinedSecondaryVertexV2Computer'),
    svComputerFatJets = cms.string('combinedSecondaryVertexV2Computer'),
    # TagInfos (need to omit the 'TagInfos' part from the label)
    ipTagInfos             = cms.string('impactParameter'),
    svTagInfos             = cms.string('inclusiveSecondaryVertexFinder'),
    softPFMuonTagInfos     = cms.string('softPFMuons'),
    softPFElectronTagInfos = cms.string('softPFElectrons'),
    # taggers
    trackCHEBJetTags    = cms.string('trackCountingHighEffBJetTags'),
    trackCNegHEBJetTags = cms.string('negativeTrackCountingHighEffJetTags'),

    trackCHPBJetTags    = cms.string('trackCountingHighPurBJetTags'),
    trackCNegHPBJetTags = cms.string('negativeTrackCountingHighPurJetTags'),

    jetBPBJetTags    = cms.string('jetBProbabilityBJetTags'),
    jetBPNegBJetTags = cms.string('negativeOnlyJetBProbabilityJetTags'),
    jetBPPosBJetTags = cms.string('positiveOnlyJetBProbabilityJetTags'),

    jetPBJetTags     = cms.string('jetProbabilityBJetTags'),
    jetPNegBJetTags  = cms.string('negativeOnlyJetProbabilityJetTags'),
    jetPPosBJetTags  = cms.string('positiveOnlyJetProbabilityJetTags'),

    simpleSVHighPurBJetTags    = cms.string('simpleSecondaryVertexHighPurBJetTags'),
    simpleSVNegHighPurBJetTags = cms.string('negativeSimpleSecondaryVertexHighPurBJetTags'),
    simpleSVHighEffBJetTags    = cms.string('simpleSecondaryVertexHighEffBJetTags'),
    simpleSVNegHighEffBJetTags = cms.string('negativeSimpleSecondaryVertexHighEffBJetTags'),

    combinedSVBJetTags    = cms.string('combinedSecondaryVertexBJetTags'),
    combinedSVPosBJetTags = cms.string('positiveCombinedSecondaryVertexBJetTags'),
    combinedSVNegBJetTags = cms.string('negativeCombinedSecondaryVertexBJetTags'),

    combinedIVFSVBJetTags    = cms.string('combinedInclusiveSecondaryVertexV2BJetTags'),
    combinedIVFSVPosBJetTags = cms.string('positiveCombinedInclusiveSecondaryVertexV2BJetTags'),
    combinedIVFSVNegBJetTags = cms.string('negativeCombinedInclusiveSecondaryVertexV2BJetTags'),

    softPFMuonBJetTags        = cms.string('softPFMuonBJetTags'),
    softPFMuonNegBJetTags     = cms.string('negativeSoftPFMuonBJetTags'),
    softPFMuonPosBJetTags     = cms.string('positiveSoftPFMuonBJetTags'),

    softPFElectronBJetTags    = cms.string('softPFElectronBJetTags'),
    softPFElectronNegBJetTags = cms.string('negativeSoftPFElectronBJetTags'),
    softPFElectronPosBJetTags = cms.string('positiveSoftPFElectronBJetTags')
)
