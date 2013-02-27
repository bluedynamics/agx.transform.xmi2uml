from xmi2_1 import XMI2_1

active_flavour=XMI2_1

def set_active_flavour(flavour):
    active_flavour=flavour
    
def get_active_flavour():
    return active_flavour

def guess_flavour(xmi):
    '''guesses the XMI Flavour, currently hardcoded to XMI2_1
    this function extracts the valid namespaces, so that the
    system is more tolerant concerning the XMI versions'''
    
    res=XMI2_1
    main=xmi.values()[-1] #XXX: assume the main xmi is the last one, is this correct?
    all=xmi.values()
    
    #main namespace
    res.XMI_NS=main.namespaces['xmi']
    res.UML_NS=main.namespaces['uml']
    
    #all possible namespaces including those from the profiles
    for node in all:
        xmi_ns=node.namespaces['xmi']
        uml_ns=node.namespaces['uml']
        if xmi_ns not in res.XMI_NS_ALT:
            res.XMI_NS_ALT.append(xmi_ns)
        if uml_ns not in res.UML_NS_ALT:
            res.UML_NS_ALT.append(uml_ns)
        
    
    return res