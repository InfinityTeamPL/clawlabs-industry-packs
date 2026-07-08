---
dataset_id: 747
file: PobierzListeMiejscowosciWGminie.pdf
file_size_mb: 0.26
institution: "Główny Urząd Statystyczny"
data_date: 2024-03-19
freshness: fresh
source_url: https://api.stat.gov.pl/
---

# PobierzListeMiejscowosciWGminie.pdf

_(z datasetu: Dostęp do danych rejestrowych TERYT poprzez usługę sieciową - interfejsy API)_

**Stron:** 2

**Treść PDF (pierwsze 20 stron, max 5000 znaków):**

Schema XML definiujący zwracany przez metodę PobierzListeMiejscowosciWGminie 
dokument XML. 
Ujęte w załączniku dane mają charakter poglądowy. 
<?xml version="1.0" encoding="utf-8"?> 
<xs:schema xmlns:a="http://schemas.datacontract.org/2004/07/TerytUslugaWs1" 
xmlns:i="http://www.w3.org/2001/XMLSchema-instance" 
xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" attributeFormDefault="unqualified" 
elementFormDefault="qualified" 
targetNamespace="http://schemas.xmlsoap.org/soap/envelope/" 
xmlns:xs="http://www.w3.org/2001/XMLSchema"> 
  <xs:import namespace="http://tempuri.org/" /> 
  <xs:element name="Envelope"> 
    <xs:complexType> 
      <xs:sequence> 
        <xs:element name="Header" /> 
        <xs:element name="Body"> 
          <xs:complexType> 
            <xs:sequence> 
              <xs:element xmlns:q1="http://tempuri.org/" 
ref="q1:PobierzListeMiejscowosciWGminieResponse" /> 
            </xs:sequence> 
          </xs:complexType> 
        </xs:element> 
      </xs:sequence> 
    </xs:complexType> 
  </xs:element> 
</xs:schema> 
<?xml version="1.0" encoding="utf-8"?> 
<xs:schema xmlns:tns="http://tempuri.org/" attributeFormDefault="unqualified" 
elementFormDefault="qualified" targetNamespace="http://tempuri.org/" 
xmlns:xs="http://www.w3.org/2001/XMLSchema"> 
  <xs:import namespace="http://schemas.datacontract.org/2004/07/TerytUslugaWs1" /> 
  <xs:element name="PobierzListeMiejscowosciWGminieResponse"> 
    <xs:complexType> 
      <xs:sequence> 
        <xs:element name="PobierzListeMiejscowosciWGminieResult"> 
          <xs:complexType> 
            <xs:sequence> 
              <xs:element 
xmlns:q1="http://schemas.datacontract.org/2004/07/TerytUslugaWs1" ref="q1:Miejscowosc" 
/> 
            </xs:sequence> 
          </xs:complexType> 
        </xs:element> 
      </xs:sequence> 
    </xs:complexType> 
  </xs:element> 
</xs:schema> 
<?xml version="1.0" encoding="utf-8"?> 
<xs:schema xmlns:tns="http://schemas.datacontract.org/2004/07/TerytUslugaWs1" 
attributeFormDefault="unqualified" elementFormDefault="qualified" 
targetNamespace="http://schemas.datacontract.org/2004/07/TerytUslugaWs1" 
xmlns:xs="http://www.w3.org/2001/XMLSchema"> 
  <xs:element name="Miejscowosc"> 
    <xs:complexType> 
      <xs:sequence> 
        <xs:element name="GmiRodzaj" type="xs:unsignedByte" /> 

        <xs:element name="GmiSymbol" type="xs:unsignedInt" /> 
        <xs:element name="Gmina" type="xs:string" /> 
        <xs:element name="Nazwa" type="xs:string" /> 
        <xs:element name="PowSymbol" type="xs:unsignedShort" /> 
        <xs:element name="Powiat" type="xs:string" /> 
        <xs:element name="Symbol" type="xs:unsignedInt" /> 
        <xs:element name="WojSymbol" type="xs:unsignedByte" /> 
        <xs:element name="Wojewodztwo" type="xs:string" /> 
      </xs:sequence> 
    </xs:complexType> 
  </xs:element> 
</xs:schema> 
Przykładowy plik xml. 
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"> 
  <s:Header /> 
  <s:Body> 
    <PobierzListeMiejscowosciWGminieResponse xmlns="http://tempuri.org/"> 
      <PobierzListeMiejscowosciWGminieResult 
xmlns:a="http://schemas.datacontract.org/2004/07/TerytUslugaWs1" 
xmlns:i="http://www.w3.org/2001/XMLSchema-instance"> 
        <a:Miejscowosc> 
          <a:GmiRodzaj>5</a:GmiRodzaj> 
          <a:GmiSymbol>1001085</a:GmiSymbol> 
          <a:Gmina>Zelów</a:Gmina> 
          <a:Nazwa>Otyk</a:Nazwa> 
          <a:PowSymbol>1001</a:PowSymbol> 
          <a:Powiat>bełchatowski</a:Powiat> 
          <a:Symbol>1038631</a:Symbol> 
          <a:WojSymbol>10</a:WojSymbol> 
          <a:Wojewodztwo>ŁÓDZKIE</a:Wojewodztwo> 
        </a:Miejscowosc> 
      </PobierzListeMiejscowosciWGminieResult> 
    </PobierzListeMiejscowosciWGminieResponse> 
  </s:Body> 
</s:Envelope> 

---
_Plik źródłowy: `data/raw/747/PobierzListeMiejscowosciWGminie.pdf` (0.26 MB) · Pobrane z https://api.stat.gov.pl/_