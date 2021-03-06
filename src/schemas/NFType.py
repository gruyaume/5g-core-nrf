from enum import Enum


class NFType(str, Enum):
    nrf = "NRF"
    udm = "UDM"
    amf = "AMF"
    smf = "SMF"
    ausf = "AUSF"
    nef = "NEF"
    pcf = "PCF"
    smsf = "SMSF"
    nssf = "NSSF"
    udr = "UDR"
    lmf = "LMF"
    gmlc = "GMLC"
    fiveg_eir = "5G_EIR"
    sepp = "SEPP"
    upf = "UPF"
    n3iwf = "N3IWF"
    af = "AF"
    udsf = "UDSF"
    bsf = "BSF"
    chf = "CHF"
    nwdaf = "NWDAF"
