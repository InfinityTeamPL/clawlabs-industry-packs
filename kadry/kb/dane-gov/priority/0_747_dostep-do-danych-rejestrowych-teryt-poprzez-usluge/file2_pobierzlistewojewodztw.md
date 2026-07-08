---
dataset_id: 747
file: PobierzListeWojewodztw.pdf
file_size_mb: 0.27
institution: "Główny Urząd Statystyczny"
data_date: 2024-03-19
freshness: fresh
source_url: https://api.stat.gov.pl/
---

# PobierzListeWojewodztw.pdf

_(z datasetu: Dostęp do danych rejestrowych TERYT poprzez usługę sieciową - interfejsy API)_

**Stron:** 2

**Treść PDF (pierwsze 20 stron, max 5000 znaków):**

Schema XML definiujący zwracany przez metodę PobierzListeWojewodztw dokument XML. 
Ujęte w załączniku dane mają charakter poglądowy. 
<?xml version="1.0" encoding="utf-8"?> 
<xs:schema xmlns:a="http://schemas.datacontract.org/2004/07/TerytUslugaWs1" 
xmlns:i="http://www.w3.org/2001/XMLSchema-instance" 
xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" attributeFormDefault="unqualified" 
elementFormDefault="qualified" 
targetNamespace="http://schemas.xmlsoap.org/soap/envelope/" 
xmlns:xs="http://www.w3.org/2001/XMLSchema"> 
  <xs:import namespace="http://schemas.microsoft.com/2004/09/ServiceModel/Diagnostics" 
/> 
  <xs:import namespace="http://tempuri.org/" /> 
  <xs:element name="Envelope"> 
    <xs:complexType> 
      <xs:sequence> 
        <xs:element name="Header"> 
          <xs:complexType> 
            <xs:sequence> 
              <xs:element 
xmlns:q1="http://schemas.microsoft.com/2004/09/ServiceModel/Diagnostics" 
ref="q1:ActivityId" /> 
            </xs:sequence> 
          </xs:complexType> 
        </xs:element> 
        <xs:element name="Body"> 
          <xs:complexType> 
            <xs:sequence> 
              <xs:element xmlns:q2="http://tempuri.org/" 
ref="q2:PobierzListeWojewodztwResponse" /> 
            </xs:sequence> 
          </xs:complexType> 
        </xs:element> 
      </xs:sequence> 
    </xs:complexType> 
  </xs:element> 
</xs:schema> 
<?xml version="1.0" encoding="utf-8"?> 
<xs:schema xmlns:tns="http://schemas.microsoft.com/2004/09/ServiceModel/Diagnostics" 
attributeFormDefault="unqualified" elementFormDefault="qualified" 
targetNamespace="http://schemas.microsoft.com/2004/09/ServiceModel/Diagnostics" 
xmlns:xs="http://www.w3.org/2001/XMLSchema"> 
  <xs:element name="ActivityId"> 
    <xs:complexType> 
      <xs:simpleContent> 
        <xs:extension base="xs:string"> 
          <xs:attribute name="CorrelationId" type="xs:string" use="required" /> 
        </xs:extension> 
      </xs:simpleContent> 
    </xs:complexType> 
  </xs:element> 
</xs:schema> 
<?xml version="1.0" encoding="utf-8"?> 
<xs:schema xmlns:tns="http://tempuri.org/" attributeFormDefault="unqualified" 
elementFormDefault="qualified" targetNamespace="http://tempuri.org/" 
xmlns:xs="http://www.w3.org/2001/XMLSchema"> 
  <xs:import namespace="http://schemas.datacontract.org/2004/07/TerytUslugaWs1" /> 
  <xs:element name="PobierzListeWojewodztwResponse"> 
    <xs:complexType> 

      <xs:sequence> 
        <xs:element name="PobierzListeWojewodztwResult"> 
          <xs:complexType> 
            <xs:sequence> 
              <xs:element maxOccurs="unbounded" 
xmlns:q1="http://schemas.datacontract.org/2004/07/TerytUslugaWs1" 
ref="q1:JednostkaTerytorialna" /> 
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
  <xs:element name="JednostkaTerytorialna"> 
    <xs:complexType> 
      <xs:sequence> 
        <xs:element name="GMI" nillable="true" /> 
        <xs:element name="NAZWA" type="xs:string" /> 
        <xs:element name="NAZWA_DOD" type="xs:string" /> 
        <xs:element name="POW" nillable="true" /> 
        <xs:element name="RODZ" nillable="true" /> 
        <xs:element name="STAN_NA" type="xs:string" /> 
        <xs:element name="WOJ" type="xs:unsignedByte" /> 
      </xs:sequence> 
    </xs:complexType> 
  </xs:element> 
</xs:schema> 
Przykładowy plik xml. 
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"> 
  <s:Header> 
    <ActivityId CorrelationId="769be38e-5c41-4e4f-9562-c72c21201ec5" 
xmlns="http://schemas.microsoft.com/2004/09/ServiceModel/Diagnostics">d54feae7-045c-
471c-b552-1bae491be76f</ActivityId> 
  </s:Header> 
  <s:Body> 
    <PobierzListeWojewodztwResponse xmlns="http://tempuri.org/"> 
      <PobierzListeWojewodztwResult 
xmlns:a="http://schemas.datacontract.org/2004/07/TerytUslugaWs1" 
xmlns:i="http://www.w3.org/2001/XMLSchema-instance"> 
        <a:JednostkaTerytorialna> 
          <a:GMI i:nil="true" /> 
          <a:NAZWA>DOLNOŚLĄSKIE</a:NAZWA> 
          <a:NAZWA_DOD>województwo</a:NAZWA_DOD> 
          <a:POW i:nil="true" /> 
          <a:RODZ i:nil="true" /> 
          <a:STAN_NA>2014-01-01 00:00:00</a:STAN_NA> 
          <a:WOJ>02</a:WOJ> 
        </a:JednostkaTerytorialna> 
      </PobierzListeWojewodztwResult> 
    </PobierzListeWojewodztwResponse> 
  </s:Body> 
</s:Envelope> 
 

---
_Plik źródłowy: `data/raw/747/PobierzListeWojewodztw.pdf` (0.27 MB) · Pobrane z https://api.stat.gov.pl/_