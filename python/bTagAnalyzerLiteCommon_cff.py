import FWCore.ParameterSet.Config as cms

from RecoBTag.SecondaryVertex.trackSelection_cff import *
from RecoBTag.SecondaryVertex.trackPseudoSelection_cff import *

trackPseudoSelectionBlock_fat= trackPseudoSelectionBlock.trackPseudoSelection.clone(jetDeltaRMax=cms.double(1))
trackSelectionBlock_fat= trackSelectionBlock.trackSelection.clone(jetDeltaRMax=cms.double(1))

bTagAnalyzerLiteCommon = cms.PSet(
    #trackPseudoSelectionBlock_fat,
    runFatJets               = cms.bool(False),
    runSubJets               = cms.bool(False),
    allowJetSkipping         = cms.bool(True),
    storeEventInfo           = cms.bool(True),
    produceJetTrackTree      = cms.bool(False), ## True if you want to keep info for tracks associated to jets
    produceJetPFLeptonTree   = cms.bool(False), ## True if you want to keep PF lepton info
    storeTagVariables        = cms.bool(False), ## True if you want to keep TagInfo TaggingVariables
    storeTagVariablesSubJets = cms.bool(False), ## True if you want to keep TagInfo TaggingVariables
    storeCSVTagVariables     = cms.bool(False),  ## True if you want to keep CSV TaggingVariables
    storeCSVTagVariablesSubJets = cms.bool(False),  ## True if you want to keep CSV TaggingVariables
    MaxEta                   = cms.double(2.5),
    MinPt                    = cms.double(20.0),
    src                      = cms.InputTag('generator'),
    BranchNamePrefix         = cms.string(''),
    Jets                     = cms.InputTag('selectedPatJets'),
    SubJets                  = cms.VInputTag(),
    SubJetLabels             = cms.vstring(),
    muonCollectionName       = cms.InputTag('muons'),
    triggerTable             = cms.InputTag('TriggerResults'),
    prunedGenParticles       = cms.InputTag('prunedGenParticlesBoost'),
    primaryVertexColl        = cms.InputTag('offlinePrimaryVertices'),
    useBCands                = cms.bool(False),
    beta                     = cms.double(1.0),
    R0                       = cms.double(0.8),
    maxSVDeltaRToJet         = cms.double(0.7),
    trackPairV0Filter = cms.PSet(k0sMassWindow = cms.double(0.03)),
    trackSort = cms.string( "sip2dSig" ),
    trackSelection = cms.PSet(
                variableJTAPars,
		totalHitsMin = cms.uint32(0),
		jetDeltaRMax = cms.double(1),
		qualityClass = cms.string('any'),
		pixelHitsMin = cms.uint32(0),
		maxDistToAxis = cms.double(0.07),
		maxDecayLen = cms.double(5),
		sip3dSigMin = cms.double(-99999.9),
		sip3dSigMax = cms.double(99999.9),
		sip2dValMax = cms.double(99999.9),
		ptMin = cms.double(0.0),
		sip2dSigMax = cms.double(99999.9),
		sip2dSigMin = cms.double(-99999.9),
		sip3dValMax = cms.double(99999.9),
		sip3dValMin = cms.double(-99999.9),
		sip2dValMin = cms.double(-99999.9),
		normChi2Max = cms.double(99999.9),
                useVariableJTA = cms.bool(False)        
                ),
#    trackSelection = cms.PSet( jetDeltaRMax=cms.double(1)),
    #pseudoVertexV0Filter = cms.PSet(k0sMassWindow = cms.double(0.05)),
    TriggerPathNames = cms.vstring(
        "HLT_HT750_v*"
    )
)
