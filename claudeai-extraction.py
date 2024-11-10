import re
from collections import defaultdict

def extract_medical_info(text):
    """
    Extrai informações médicas como medicamentos, exames e doenças de um texto.
    
    Args:
        text (str): O texto do documento médico.
        
    Returns:
        dict: Um dicionário contendo as informações extraídas.
    """
    medications = extract_medications(text)
    tests = extract_medical_tests(text)
    conditions = extract_medical_conditions(text)
    
    return {
        "medications": medications,
        "tests": tests,
        "conditions": conditions
    }

def extract_medications(text):
    """
    Extrai os medicamentos mencionados no texto.
    
    Args:
        text (str): O texto do documento médico.
        
    Returns:
        list: Uma lista de medicamentos extraídos.
    """
    medication_patterns = [
        r"\b(?:medication|drug|prescribed)\s*:\s*(\w+(?:\s\w+)*)",
        r"\b(\w+(?:\s\w+)*)\s*medication"
    ]
    
    medications = []
    for pattern in medication_patterns:
        medications.extend(re.findall(pattern, text, re.IGNORECASE))
    
    return list(set(medications))

def extract_medical_tests(text):
    """
    Extrai os exames médicos mencionados no texto.
    
    Args:
        text (str): O texto do documento médico.
        
    Returns:
        list: Uma lista de exames médicos extraídos.
    """
    test_patterns = [
        r"\b([\w\s]+)\s*test\b",
        r"\b([\w\s]+)\s*exam\b"
    ]
    
    tests = []
    for pattern in test_patterns:
        tests.extend(re.findall(pattern, text, re.IGNORECASE))
    
    return list(set(tests))

def extract_medical_conditions(text):
    """
    Extrai as condições médicas ou doenças mencionadas no texto.
    
    Args:
        text (str): O texto do documento médico.
        
    Returns:
        dict: Um dicionário com as condições médicas e suas frequências.
    """
    condition_patterns = [
        r"\b([\w\s]+)\s*condition\b",
        r"\b([\w\s]+)\s*disease\b",
        r"\b([\w\s]+)\s*disorder\b"
    ]
    
    conditions = defaultdict(int)
    for pattern in condition_patterns:
        for condition in re.findall(pattern, text, re.IGNORECASE):
            conditions[condition] += 1
    
    return dict(conditions)

# Exemplo de uso
sample_text = """
O paciente apresenta quadro de pressão alta (hipertensão) e necessita realizar exame de ressonância magnética. Foi prescrito o medicamento Lisinopril para controle da pressão.
"""

medical_info = extract_medical_info(sample_text)
print(medical_info)
