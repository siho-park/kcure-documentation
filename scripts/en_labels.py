# -*- coding: utf-8 -*-
"""English names for dictionary labels. Korean that the glossary already
translates is left to ko_glossary; this module covers the variable names.
"""
from __future__ import annotations

import re

# Longer phrases first. These are names and finding labels from dictionary v4.0.
STEMS = {
    "국제질병분류코드": "ICD-10 code",
    "원발부위코드": "Primary site code",
    "조직학적진단그룹": "Histologic diagnosis group",
    "최종진단방법": "Most definitive method of diagnosis",
    "'99-'11년 암진단 여부": "Cancer diagnosed in 1999–2011",
    "명세서조인키": "Claim join key",
    "보험자종별 구분코드": "Insurer type",
    "수진자연령": "Patient's age",
    "요양기관식별대체키": "Provider substitute identifier",
    "요양기관종별 구분코드": "Provider type",
    "요양기관기호 지역구분코드": "Provider region",
    "서식구분코드": "Claim form type",
    "주상병코드": "Primary diagnosis code",
    "부상병코드": "Secondary diagnosis code",
    "진료과목코드": "Specialty code",
    "요양개시일자": "Care start date",
    "요양종료일자": "Care end date",
    "최초입원일자": "First admission date",
    "입내원일수": "Days of visit or admission",
    "요양일수": "Days of care",
    "원외처방일수": "Outpatient prescription days",
    "원외처방약제비": "Outpatient prescription drug cost",
    "원외처방전건수": "Number of outpatient prescriptions",
    "심사결정요양 급여비용총액": "Reviewed total benefit cost",
    "심사결정 본인부담금": "Reviewed patient copayment",
    "심사결정 보험자부담금": "Reviewed insurer payment",
    "심사결정100분의 100미만총액": "Reviewed total under the 100-percent copayment",
    "수술여부": "Surgery",
    "공상구분코드": "Official injury or illness category",
    "특정기호구분코드": "Special symbol code",
    "상해외인 구분코드": "External cause of injury",
    "진료결과 구분코드": "Discharge status",
    "입원도착경로 구분코드": "Route of admission",
    "의료급여 종별코드": "Medical Aid category",
    "청구형태코드": "Claim form code",
    "청구구분코드": "Claim type code",
    "1_2구분코드": "Primary or secondary classification",
    "1일투약량": "Daily dose",
    "1일투여량 또는 실시횟수": "Daily dose or number of times performed",
    "1회투약량": "Dose per administration",
    "총투여일수 또는 실시횟수": "Total days of administration or number of times performed",
    "총사용량": "Total amount used",
    "단가": "Unit price",
    "금액": "Amount",
    "가산적용금액": "Amount after the add-on",
    "일반명코드": "Ingredient code",
    "줄번호": "Line number",
    "일련번호": "Sequence number",
    "분류코드": "Classification code",
    "분류코드구분": "Classification-code type",
    "상병분류구분": "Diagnosis classification type",
    "상병코드": "Diagnosis code",
    "항목코드": "Item code",
    "처방전교부번호": "Prescription issue number",
    "표시과목코드": "Listed specialty code",
    "내과세부전문과목": "Internal-medicine subspecialty",
    "진료예외 구분코드": "Exceptional care type",
    "심사연월": "Review year and month",
    "근무구분코드": "Work type",
    "가입자구분": "Insurance-status category",
    "보험료": "Insurance premium decile",
    "증인원수": "Number of people on the insurance card",
    "종합장애등급코드": "Overall disability grade",
    "주장애유형": "Main disability type",
    "사망연월일": "Date of death",
    "사망원인코드1": "Underlying cause of death",
    "사망원인코드2": "External cause of death",
    "최초진단연월일": "Date of first diagnosis",
    "진단시 만나이": "Age in full years at diagnosis",
    "요약병기": "SEER summary stage",
    "실거주주소코드": "Province of residence",
    "기준연도": "Reference year",
    "검진사업연도": "Screening year",
    "성별": "Sex",
    "치료": "Treatment",
    "신장": "Height",
    "체중": "Weight",
    "체질량지수": "Body mass index",
    "허리둘레": "Waist circumference",
    "수축기혈압": "Systolic blood pressure",
    "이완기혈압": "Diastolic blood pressure",
    "공복혈당": "Fasting glucose",
    "총콜레스테롤": "Total cholesterol",
    "트리글리세라이드": "Triglyceride",
    "HDL콜레스테롤": "HDL cholesterol",
    "LDL콜레스테롤": "LDL cholesterol",
    "혈색소": "Hemoglobin",
    "요단백": "Urine protein",
    "요당": "Urine glucose",
    "요잠혈": "Urine occult blood",
    "혈청크레아티닌": "Serum creatinine",
    "신사구체여과율(GFR)": "Glomerular filtration rate (GFR)",
    "감마지티피": "Gamma-glutamyl transferase",
    "(혈청지오티)AST": "AST (SGOT)",
    "(혈청지피티)ALT": "ALT (SGPT)",
    "확진일자": "Confirmation date",
    "감염경로": "Route of infection",
    "신고기관시도": "Reporting province",
    "신고기관권역": "Reporting region",
    "접종일자": "Vaccination date",
    "접종차수": "Dose number",
    "접종백신명": "Vaccine name",
    "기존 간암환자": "Already a liver-cancer patient",
    "기존 대장암환자": "Already a colorectal-cancer patient",
    "기존 유방암환자": "Already a breast-cancer patient",
    "기존 위암환자": "Already a stomach-cancer patient",
    "간암 진찰료포함여부": "Liver-cancer consultation fee included",
    "대장암 진찰료포함여부": "Colorectal-cancer consultation fee included",
    "유방암 진찰료포함여부": "Breast-cancer consultation fee included",
    "자궁경부암 진찰료포함여부": "Cervical-cancer consultation fee included",
    "위암진찰료포함여부": "Stomach-cancer consultation fee included",
    "간암종합판정": "Overall liver-cancer judgment",
    "대장암종합판정": "Overall colorectal-cancer judgment",
    "유방암종합판정": "Overall breast-cancer judgment",
    "자궁경부암종합판정": "Overall cervical-cancer judgment",
    "위암종합판정": "Overall stomach-cancer judgment",
    "위 조직진단결과": "Stomach histologic result",
    "위 조직진단필요": "Stomach histology needed",
    "조직검사 결과": "Biopsy result",
    "조직검사 필요": "Biopsy needed",
    "조직진단필요여부": "Histology needed",
    "대장 조직진단": "Colorectal histologic diagnosis",
    "병리조직검사 개수": "Number of pathology specimens",
    "병리조직진단 개수": "Number of histologic diagnoses",
    "유방단순촬영 조직검사실시여부": "Biopsy performed at mammography",
    "유방실질 분포량": "Amount of fibroglandular tissue",
    "유방암 검사방법": "Breast-screening method",
    "촬영부위 구분": "Imaging site",
    "대장암 분변잠혈반응검사 결과(음성, 양성)": "Fecal occult blood result (negative or positive)",
    "대장암 분변잠혈반응검사 방법": "Fecal occult blood method",
    "대장암 분변잠혈반응검사 방법(정성, 정량)": "Fecal occult blood method (qualitative or quantitative)",
    "대장이중조영검사 검사방법": "Double-contrast barium enema method",
    "위장조영검사 검사방법": "Upper GI series method",
    "관찰소견 대장용종_절제처치 실시 유무": "Polyp removed during the examination",
    "관찰소견 간암의심 병변크기": "Suspected liver cancer, lesion size",
    "간초음파검사 병변크기": "Liver ultrasound, lesion size",
    "대장내시경검사 관찰소견_대장용종크기": "Colonoscopy, polyp size",
    "자궁경부세포검사 검체상태": "Cervical cytology, specimen adequacy",
    "자궁경부세포검사 선상피세포": "Cervical cytology, glandular cells",
    "자궁경부세포검사 유형별진단(세포진단)": "Cervical cytology, diagnosis by cell type",
    "자궁경부세포검사 추가소견": "Cervical cytology, additional finding",
    "유형별진단 비정형 선상피세포 위험구분": "Atypical glandular cells, risk category",
    "유형별진단 비정형 편평상피세포 위험구분": "Atypical squamous cells, risk category",
    "유형별진단 선상피세포 이상": "Glandular-cell abnormality",
    "유형별진단 편평상피세포 이상": "Squamous-cell abnormality",
    "혈청알파태아단백검사_01. AFP 검사방법": "AFP test method",
    "혈청알파태아단백검사_02. 결과(정성법)": "AFP result (qualitative)",
    "혈청알파태아단백검사_03. 수치(정량법)": "AFP value (quantitative)",
    "혈청알파태아단백검사_04. 단위(정량법)": "AFP unit (quantitative)",
    "혈청알파태아단백검사_05. 기준치(정량법)": "AFP reference value (quantitative)",
    "고위험군선별검사_01. ALT(SGPT)": "High-risk screening: ALT (SGPT)",
    "고위험군선별검사_02. B형 간염바이러스표면항원(HBsAg) 검사방법": "HBsAg test method",
    "고위험군선별검사_03. B형 간염바이러스표면항원(HBsAg) 검사결과": "HBsAg result",
    "고위험군선별검사_04. C형 간염바이러스항체(Anti-HCV) 검사방법": "Anti-HCV test method",
    "고위험군선별검사_05. C형 간염바이러스항체 (Anti-HCV) 검사결과": "Anti-HCV result",
    "고위험군선별검사_06. C형 간염바이러스항체 (Anti-HCV) 정밀 검사수치": "Anti-HCV confirmatory value",
    "고위험군선별검사_07. C형 간염바이러스항체 (Anti-HCV) 정밀 기준치": "Anti-HCV confirmatory reference value",
    "고위험군선별검사_08. C형 간염바이러스항체 (Anti-HCV) 판정": "Anti-HCV judgment",
    "간초음파검사": "Liver ultrasound",
    "대장이중조영검사": "Double-contrast barium enema",
    "대장내시경검사": "Colonoscopy",
    "위장조영검사": "Upper GI series",
    "위장조영촬영": "Upper GI series",
    "상부소화관내시경": "Upper endoscopy",
    "위내시경": "Gastroscopy",
    "유방단순촬영": "Mammography",
    "유방촬영": "Mammography",
    "결장이중조영촬영": "Double-contrast barium enema",
    "결장경검사": "Colonoscopy",
    "단순촬영": "Plain radiography",
    "관찰소견": "Observation",
    "판독소견": "Reading",
    "검사소견": "Examination finding",
    "병변위치": "Lesion site",
    "병변부위": "Lesion site",
    "병형 기타": "Finding, other",
    "병형기타": "other finding",
    "병형": "Finding type",
    "만성간질환": "Chronic liver disease",
    "문맥침범": "Portal-vein involvement",
    "간암형": "Liver-cancer pattern",
    "간종괴(1CM 미만)": "Liver mass smaller than 1 cm",
    "간종괴(1CM 이상)": "Liver mass of 1 cm or larger",
    "간암의심": "Suspected liver cancer",
    "양성질환": "Benign disease",
    "조직진단 기타": "Histologic diagnosis, other",
    "조직진단 암": "Histologic diagnosis, cancer",
    "조직진단": "Histologic diagnosis",
    "직접기입": "written in directly",
    "직접기술": "written in directly",
    "위저부": "gastric fundus",
    "위체부": "gastric body",
    "위전정부": "gastric antrum",
    "위분문부": "gastric cardia",
    "분문부": "cardia",
    "소만": "lesser curvature",
    "대만": "greater curvature",
    "전벽": "anterior wall",
    "후벽": "posterior wall",
    "회장 말단부": "terminal ileum",
    "맹장": "cecum",
    "상행 결장": "ascending colon",
    "간 만곡": "hepatic flexure",
    "횡행 결장": "transverse colon",
    "비 만곡": "splenic flexure",
    "하행 결장": "descending colon",
    "에스 결장": "sigmoid colon",
    "직장": "rectum",
    "항문": "anus",
    "왼쪽 상외측": "left upper outer quadrant",
    "왼쪽 상내측": "left upper inner quadrant",
    "왼쪽 하외측": "left lower outer quadrant",
    "왼쪽 하내측": "left lower inner quadrant",
    "왼쪽 유두하부": "left subareolar",
    "왼쪽 액와부": "left axilla",
    "왼쪽 직접기입": "left, written in directly",
    "오른쪽 상외측": "right upper outer quadrant",
    "오른쪽 상내측": "right upper inner quadrant",
    "오른쪽 하외측": "right lower outer quadrant",
    "오른쪽 하내측": "right lower inner quadrant",
    "오른쪽 유두하부": "right subareolar",
    "오른쪽 액와부": "right axilla",
    "오른쪽 직접기입": "right, written in directly",
    "좌상외": "left upper outer",
    "좌상내": "left upper inner",
    "좌하외": "left lower outer",
    "좌하내": "left lower inner",
    "좌유륜": "left areola",
    "우유륜": "right areola",
    "우상외": "right upper outer",
    "우상내": "right upper inner",
    "우하외": "right lower outer",
    "우하내": "right lower inner",
    "좌12시": "left 12 o'clock",
    "좌3시": "left 3 o'clock",
    "좌6시": "left 6 o'clock",
    "좌9시": "left 9 o'clock",
    "우12시": "right 12 o'clock",
    "우3시": "right 3 o'clock",
    "우6시": "right 6 o'clock",
    "우9시": "right 9 o'clock",
    "단발성 결정형": "single nodular",
    "다발성 결정형": "multinodular",
    "대종괴형": "massive",
    "미만형": "diffuse",
    "주문맥": "main portal vein",
    "좌문맥": "left portal vein",
    "우문맥": "right portal vein",
    "만성간염": "chronic hepatitis",
    "간경변증": "cirrhosis",
    "간경화": "cirrhosis",
    "지방간": "fatty liver",
    "간염": "hepatitis",
    "담석증": "gallstones",
    "간디스토마": "clonorchiasis",
    "급성알코올간염": "acute alcoholic hepatitis",
    "간종대": "hepatomegaly",
    "비종대": "splenomegaly",
    "간경색증": "hepatic infarction",
    "담관의 결석": "bile-duct stone",
    "담낭염": "cholecystitis",
    "신결석": "renal stone",
    "담낭의 천공": "gallbladder perforation",
    "담관유착": "bile-duct adhesion",
    "간의 악성신생물": "malignant neoplasm of the liver",
    "간의 양성신생물": "benign neoplasm of the liver",
    "췌장의 양성신생물": "benign neoplasm of the pancreas",
    "신낭종": "renal cyst",
    "간석회화": "hepatic calcification",
    "간하수증": "hepatoptosis",
    "양성신생물": "benign neoplasm",
    "담낭낭종": "gallbladder cyst",
    "간내혈관종": "intrahepatic hemangioma",
    "담낭비후": "gallbladder-wall thickening",
    "용종": "polyp",
    "간내담관결석": "intrahepatic bile-duct stone",
    "간문맥 혹은 간정맥 혈전": "portal-vein or hepatic-vein thrombus",
    "담낭이상(직접기술)": "gallbladder abnormality, written in directly",
    "담관확장": "bile-duct dilatation",
    "간내 석회화": "intrahepatic calcification",
    "복수": "ascites",
    "비장종대": "splenomegaly",
    "혈관종": "hemangioma",
    "간낭종": "hepatic cyst",
    "에스결장다발성게실": "multiple sigmoid diverticula",
    "대장염": "colitis",
    "치질": "hemorrhoids",
    "항문및직장의용종": "polyp of the anus or rectum",
    "특발성항문대장염": "idiopathic proctocolitis",
    "변비": "constipation",
    "직장의악성신생물": "malignant neoplasm of the rectum",
    "치핵": "hemorrhoids",
    "비특이성 장염": "nonspecific colitis",
    "허혈성 장염": "ischemic colitis",
    "궤양성 대장염": "ulcerative colitis",
    "크론병": "Crohn's disease",
    "장결핵": "intestinal tuberculosis",
    "대장 게실증": "colonic diverticulosis",
    "림프구 증식": "lymphoid hyperplasia",
    "식도/위 정맥류": "esophageal or gastric varices",
    "식도염": "esophagitis",
    "식도게실": "esophageal diverticulum",
    "식도암": "esophageal cancer",
    "식도 점막하종양": "esophageal submucosal tumor",
    "식도 암종": "esophageal carcinoma",
    "급성위염": "acute gastritis",
    "만성위염": "chronic gastritis",
    "위게실": "gastric diverticulum",
    "십이지장염": "duodenitis",
    "십이지장게실": "duodenal diverticulum",
    "십이지장 궤양": "duodenal ulcer",
    "십이지장 악성종양": "malignant tumor of the duodenum",
    "십이지장 점막하종양": "duodenal submucosal tumor",
    "십이지장 암종": "duodenal carcinoma",
    "신경내분비종양": "neuroendocrine tumor",
    "위의 비상피성종양": "nonepithelial tumor of the stomach",
    "비상피성종양": "nonepithelial tumor",
    "항문암": "anal cancer",
    "말단회장부위 암": "cancer of the terminal ileum",
    "관상샘암종(고분화/중분화/저분 화)": "tubular adenocarcinoma (well, moderately, or poorly differentiated)",
    "관상샘암종(고분화)": "tubular adenocarcinoma, well differentiated",
    "관상샘암종(중분화)": "tubular adenocarcinoma, moderately differentiated",
    "관상샘암종(저분화)": "tubular adenocarcinoma, poorly differentiated",
    "샘암종 (고분화, 중분화, 저분화)": "adenocarcinoma (well, moderately, or poorly differentiated)",
    "샘암종 (고분화)": "adenocarcinoma, well differentiated",
    "샘암종 (중분화)": "adenocarcinoma, moderately differentiated",
    "샘암종 (저분화)": "adenocarcinoma, poorly differentiated",
    "유두상샘암종": "papillary adenocarcinoma",
    "점액(샘)암종": "mucinous adenocarcinoma",
    "반지세포암종": "signet-ring cell carcinoma",
    "샘편평상피암종": "adenosquamous carcinoma",
    "위림프종(저도/고도)": "gastric lymphoma (low or high grade)",
    "위림프종(고도)": "gastric lymphoma, high grade",
    "위림프종(저도)": "gastric lymphoma, low grade",
    "편평상피암종": "squamous cell carcinoma",
    "소세포암종": "small cell carcinoma",
    "수질암종": "medullary carcinoma",
    "미분화암종": "undifferentiated carcinoma",
    "악성림프종": "malignant lymphoma",
    "부위": "site",
    "기타": "other",
    "정상": "normal",
    "간질환": "liver disease",
    "중풍": "stroke",
    "심근경색": "myocardial infarction",
    "협심증": "angina",
    "B형간염바이러스보유자": "hepatitis B virus carrier",
    "C형간염바이러스보유자": "hepatitis C virus carrier",
    "만성B형간염": "chronic hepatitis B",
    "만성C형간염": "chronic hepatitis C",
    "위투시촬영": "upper GI series",
    "대변잠혈검사": "fecal occult blood test",
    "대장내시경": "colonoscopy",
    "간초음파": "liver ultrasound",
    "유방엑스선검사": "mammography",
    "자궁경부세포검사": "cervical cytology",
    "흉부CT": "chest CT",
    "위축성 위염": "atrophic gastritis",
    "장상피화생": "intestinal metaplasia",
    "위용종": "gastric polyp",
    "대장용종": "colorectal polyp",
    "치열": "anal fissure",
    "만성폐쇄성폐질환": "chronic obstructive pulmonary disease",
    "만성기관지염": "chronic bronchitis",
    "폐기종": "emphysema",
    "폐결절": "lung nodule",
    "간질성폐질환": "interstitial lung disease",
    "진폐증": "pneumoconiosis",
    "위장질환": "gastrointestinal disease",
    "폐질환": "lung disease",
    "기타(암포함)": "other, including cancer",
}

# Full labels whose wording does not fall out of the phrase list.
FULL = {
    "[문진1] (본인) 뇌졸중(중풍) 진단여부": "Questionnaire 1: own history of stroke, diagnosed",
    "[문진1] (본인) 심장병(심근경색/협심증) 진단여부": "Questionnaire 1: own history of heart disease (myocardial infarction or angina), diagnosed",
    "[문진1] (본인) 뇌졸중(중풍) 약물치료여부": "Questionnaire 1: own history of stroke, treated with medication",
    "[문진1] (본인) 심장병(심근경색/협심증) 약물치료여부": "Questionnaire 1: own history of heart disease (myocardial infarction or angina), treated with medication",
    "[문진1] (본인) 고혈압 약물치료여부": "Questionnaire 1: own history of hypertension, treated with medication",
    "[문진1] (본인) 당뇨병 약물치료여부": "Questionnaire 1: own history of diabetes, treated with medication",
    "[문진1] (본인) 이상지질혈증 약물치료여부": "Questionnaire 1: own history of dyslipidemia, treated with medication",
    "[문진1] (본인) 폐결핵 약물치료여부": "Questionnaire 1: own history of pulmonary tuberculosis, treated with medication",
    "[문진1] (본인) 기타(암포함) 약물치료여부": "Questionnaire 1: own history of another condition, including cancer, treated with medication",
    "[문진6] 간 질환이 있으십니까? -B형간염바이러스보유자": "Questionnaire 6: do you have liver disease? Hepatitis B virus carrier",
    "[문진6] 간 질환이 있으십니까? -C형간염바이러스보유자": "Questionnaire 6: do you have liver disease? Hepatitis C virus carrier",
    "[문진6] 간 질환이 있으십니까? -만성B형간염": "Questionnaire 6: do you have liver disease? Chronic hepatitis B",
    "[문진6] 간 질환이 있으십니까? -만성C형간염": "Questionnaire 6: do you have liver disease? Chronic hepatitis C",
    "[문진6] 간 질환이 있으십니까? -간경화/간경변": "Questionnaire 6: do you have liver disease? Cirrhosis",
    "[문진7] 간 질환이 있으십니까? -B형간염바이러스보유자": "Questionnaire 7: do you have liver disease? Hepatitis B virus carrier",
    "[문진7] 간 질환이 있으십니까? -만성B형간염": "Questionnaire 7: do you have liver disease? Chronic hepatitis B",
    "[문진7] 간 질환이 있으십니까? -만성C형간염": "Questionnaire 7: do you have liver disease? Chronic hepatitis C",
    "[문진7] 간 질환이 있으십니까? -간경화/간경변": "Questionnaire 7: do you have liver disease? Cirrhosis",
    "[문진16] 암과 관련된 검사경험 -위투시촬영(UGI)유무": "Questionnaire 16: ever had a cancer-related test, upper GI series (UGI)",
    "[문진16] 암과 관련된 검사경험 -대변잠혈검사유무": "Questionnaire 16: ever had a cancer-related test, fecal occult blood test",
    "[문진16] 암과 관련된 검사경험 -대장이중조영검사(대장 x선 촬영)": "Questionnaire 16: ever had a cancer-related test, double-contrast barium enema",
    "[문진16] 암과 관련된 검사경험 -대장내시경유무": "Questionnaire 16: ever had a cancer-related test, colonoscopy",
    "[문진16] 암과 관련된 검사경험 -간초음파": "Questionnaire 16: ever had a cancer-related test, liver ultrasound",
    "[문진23] 암과 관련된 검사경험 -유방엑스선검사유무": "Questionnaire 23: ever had a cancer-related test, mammography",
    "[문진23] 암과 관련된 검사경험 -자궁경부세포검사": "Questionnaire 23: ever had a cancer-related test, cervical cytology",
    "[문진4] 암과 관련된 검사경험 -위투시촬영(UGI)유무": "Questionnaire 4: ever had a cancer-related test, upper GI series (UGI)",
    "[문진4] 암과 관련된 검사경험 -유방엑스선검사유무": "Questionnaire 4: ever had a cancer-related test, mammography",
    "[문진4] 암과 관련된 검사경험 -대변잠혈검사유무": "Questionnaire 4: ever had a cancer-related test, fecal occult blood test",
    "[문진4] 암과 관련된 검사경험 -대장이중조영검사(대장 x선 촬영)": "Questionnaire 4: ever had a cancer-related test, double-contrast barium enema",
    "[문진4] 암과 관련된 검사경험 -대장내시경유무": "Questionnaire 4: ever had a cancer-related test, colonoscopy",
    "[문진4] 암과 관련된 검사경험 -자궁경부세포검사": "Questionnaire 4: ever had a cancer-related test, cervical cytology",
    "[문진4] 암과 관련된 검사경험 -간초음파": "Questionnaire 4: ever had a cancer-related test, liver ultrasound",
    "[문진4] 암과 관련된 검사경험 -흉부CT": "Questionnaire 4: ever had a cancer-related test, chest CT",
    "[문진5] 현재 또는 과거에 진단받은 위장질환이 있으십니까? -위궤양": "Questionnaire 5: diagnosed now or in the past with gastrointestinal disease? Gastric ulcer",
    "[문진5] 현재 또는 과거에 진단받은 위장질환이 있으십니까? -위축성 위염": "Questionnaire 5: diagnosed now or in the past with gastrointestinal disease? Atrophic gastritis",
    "[문진5] 현재 또는 과거에 진단받은 위장질환이 있으십니까? -장상피화생": "Questionnaire 5: diagnosed now or in the past with gastrointestinal disease? Intestinal metaplasia",
    "[문진5] 현재 또는 과거에 진단받은 위장질환이 있으십니까? -위용종": "Questionnaire 5: diagnosed now or in the past with gastrointestinal disease? Gastric polyp",
    "[문진5] 현재 또는 과거에 진단받은 위장질환이 있으십니까? -기타": "Questionnaire 5: diagnosed now or in the past with gastrointestinal disease? Other",
    "[문진6] 현재 또는 과거에 진단받은 대장항문 질환이 있으십니까?-대장용종(폴립)": "Questionnaire 6: diagnosed now or in the past with colorectal or anal disease? Colorectal polyp",
    "[문진6] 현재 또는 과거에 진단받은 대장항문 질환이 있으십니까?-궤양성 대장염": "Questionnaire 6: diagnosed now or in the past with colorectal or anal disease? Ulcerative colitis",
    "[문진6] 현재 또는 과거에 진단받은 대장 항문질환이 있으십니까?-크론병": "Questionnaire 6: diagnosed now or in the past with colorectal or anal disease? Crohn's disease",
    "[문진6] 현재 또는 과거에 진단받은 대장 항문질환이 있으십니까?-치질(치핵,치열)": "Questionnaire 6: diagnosed now or in the past with colorectal or anal disease? Hemorrhoids or anal fissure",
    "[문진6] 현재 또는 과거에 진단받은 대장 항문질환이 있으십니까?-기타": "Questionnaire 6: diagnosed now or in the past with colorectal or anal disease? Other",
    "[문진8] 현재 또는 과거에 진단받은 폐질환이 있으십니까? -만성폐쇄성폐질환(만성기관지염, 폐기종 등)": "Questionnaire 8: diagnosed now or in the past with lung disease? Chronic obstructive pulmonary disease (chronic bronchitis, emphysema, and related conditions)",
    "[문진8] 현재 또는 과거에 진단받은 폐질환이 있으십니까? -폐결핵": "Questionnaire 8: diagnosed now or in the past with lung disease? Pulmonary tuberculosis",
    "[문진8] 현재 또는 과거에 진단받은 폐질환이 있으십니까? -폐결절": "Questionnaire 8: diagnosed now or in the past with lung disease? Lung nodule",
    "[문진8] 현재 또는 과거에 진단받은 폐질환이 있으십니까? -간질성폐질환": "Questionnaire 8: diagnosed now or in the past with lung disease? Interstitial lung disease",
    "[문진8] 현재 또는 과거에 진단받은 폐질환이 있으십니까? -진폐증": "Questionnaire 8: diagnosed now or in the past with lung disease? Pneumoconiosis",
    "[문진8] 현재 또는 과거에 진단받은 폐질환이 있으십니까? -기타": "Questionnaire 8: diagnosed now or in the past with lung disease? Other",
    "간초음파검사 병형 기타_02. 간질환": "Liver ultrasound, other finding 02, liver disease",
    "조직진단 기타_08. 직접기입": "Histologic diagnosis, other 08, written in directly",
    "자료등록연도": "Year the record was registered",
    "최초진단연월": "Year and month of first diagnosis",
    "조직학적진단코드": "Histology code",
    "분화도": "Grade",
    "종양의 크기 원발종양의 최대길이 또는 최대직경": "Size of the primary tumor, maximum length or diameter",
    "종양이 퍼진 정도-원발부위 내 종양침범 또는 인접 기관 내에 직접 침범 유무": "Extension of the primary tumor, within the organ or into an adjacent organ",
    "종양의 크기와 퍼진 정도의 결정 방법": "How size and extension were determined",
    "침범된 국소림프절-침범된 종류, 범위": "Regional nodes involved, and the kind and extent of involvement",
    "국소림프절 침범 여부의 결정 방법": "How node involvement was determined",
    "병리검사 결과 양성으로 진단된 국소림프절의 개수": "Number of regional nodes positive on pathology",
    "병리검사에서 검사된 국소림프절의 총 개수": "Number of regional nodes examined",
    "원격전이 부위": "Site of distant metastasis",
    "원격전이 부위의 결정 방법": "How the metastatic site was determined",
    "임상적 TNM": "Clinical TNM",
    "임상적 stage": "Clinical stage",
    "금연 시작 연도": "Year smoking stopped",
    "흡연량": "Amount smoked",
    "흡연기간": "Duration of smoking",
    "조직진단명_1": "Histologic diagnosis 1",
    "조직진단명_2": "Histologic diagnosis 2",
    "조직진단명_3": "Histologic diagnosis 3",
    "조직진단명_4": "Histologic diagnosis 4",
    "조직진단명_5": "Histologic diagnosis 5",
    "조직진단명_6": "Histologic diagnosis 6",
    "조직진단명_7": "Histologic diagnosis 7",
    "조직진단명_기타": "Histologic diagnosis, other",
    "영상진단소견_T인자": "Imaging T",
    "영상진단소견_N인자": "Imaging N",
    "영상진단소견_M인자": "Imaging M",
    "조직학적진단소견_T인자": "Pathologic T",
    "조직학적진단소견_N인자": "Pathologic N",
    "조직학적진단소견_M인자": "Pathologic M",
    "가입자 구분": "Eligibility type",
}

_STEMS = sorted(STEMS.items(), key=lambda kv: len(kv[0]), reverse=True)
_HANGUL = re.compile(r"[가-힣]")

_DRINK = {"소주": "soju", "맥주": "beer", "양주": "spirits", "막걸리": "makgeolli", "와인": "wine"}
_UNIT = {"잔": "glasses", "병": "bottles", "캔": "cans", "cc": "cc"}

_Q_EXACT = {
    "1주 운동횟수": "days of exercise in a week",
    "폐경 나이": "age at menopause",
    "외식을 하실 때 음식의 간에 대해 어떻게 느끼십니까?": "When you eat out, how salty does the food taste?",
    "최근 1주일 동안 팔굽혀펴기, 윗몸일으키기, 아령, 역기, 철봉 등 근력 운동을 한 날은 며칠입니까?-주당 _일": "In the past week, on how many days did you do strength exercise such as push-ups, sit-ups, dumbbells, weights, or a pull-up bar? Days per week",
    "현재 월경의 상태는 어떠십니까?": "What is your current menstrual status?",
    "담배를 끊은 지 _년 되었음": "Years since quitting cigarettes",
    "귀하는 지금까지 평생 총 20갑(400개피) 이상의 담배를 피운 적이 있습니까?": "Have you smoked 20 packs (400 cigarettes) or more in your lifetime?",
    "정신건강/스트레스": "Mental health and stress",
    "폐경 후 증상을 완화하기 위해서 호르몬 제제를 복용하고 계시거나 과거에 복용하신 적이 있습니까?": "Are you taking, or have you taken, hormones for symptoms after menopause?",
    "_세부터": "From age _",
    "총 _년간": "For _ years in total",
    "하루 평균 _개피 피웠음": "Cigarettes per day, on average",
    "하루 30분 이상 약간 숨이 찰 정도로 걷거나 운동 하기를 일주일에 몇 일 정도 하십니까?": "On how many days a week do you walk or exercise for at least 30 minutes, enough to be slightly short of breath?",
    "음주를 끊은 지 _년 되었음": "Years since quitting alcohol",
    "현재 귀하의 음주상태는 어떻습니까?": "What is your current drinking status?",
    "한번 마실때, 평균 어느 정도 마십니까? (소주 2홉 1병 기준으로)": "When you drink, how much do you usually drink? (one 360 ml bottle of soju as the unit)",
    "음주 횟수는?": "How often do you drink?",
    "피임약을 복용하고 계시거나 과거에 복용하신 적이 있습니까?": "Are you taking, or have you taken, oral contraceptives?",
    "월경을 언제 시작하셨습니까?": "When did your periods start?",
    "초경 시작 나이": "Age at menarche",
    "(본인)과거병력코드1": "Own past-history code 1",
    "(본인)과거병력코드2": "Own past-history code 2",
    "(본인)과거병력코드3": "Own past-history code 3",
    "(본인)과거질환발생연도1": "Year of own past illness 1",
    "(본인)과거질환발생연도2": "Year of own past illness 2",
    "(본인)과거질환발생연도3": "Year of own past illness 3",
    "(본인)과거질환완치유무1": "Own past illness 1 resolved",
    "(본인)과거질환완치유무2": "Own past illness 2 resolved",
    "(본인)과거질환완치유무3": "Own past illness 3 resolved",
    "(부모) 과거병력 유무": "Past history in a parent",
    "(자녀) 과거병력 유무": "Past history in a child",
    "(자매) 과거병력 유무": "Past history in a sister",
    "(형제) 과거병력 유무": "Past history in a brother",
    "폐암 유무": "Lung cancer",
    "간암 유무": "Liver cancer",
    "기타 유무": "Other",
    "대장암 유무": "Colorectal cancer",
    "위암 유무": "Stomach cancer",
    "유방암 유무": "Breast cancer",
    "자궁경부암 유무": "Cervical cancer",
    "(과거)금연전 흡연기간": "Years smoked before quitting",
    "(과거)금연전 하루흡연량": "Cigarettes per day before quitting",
    "(현재)하루흡연량": "Cigarettes per day, current",
    "(현재)흡연기간": "Years smoked, current",
    "(과거,현재)흡연기간": "Years smoked, past or current",
    "영양섭취행태": "Diet",
    "주간음주일수": "Drinking days per week",
    "1회 음주량": "Amount per drinking occasion",
    "음주습관": "Drinking habit",
    "흡연여부": "Smoking status",
    "현재 신체 어느 부위에든 불편한 증상이 있습니까?": "Do you have an uncomfortable symptom anywhere in your body?",
    "(체중감소인 경우)감소 체중": "Kilograms lost, if weight was lost",
    "최근 6개월 간 특별한 이유 없이 5kg 이상의 체중감소가 있었습니까?": "In the past 6 months, have you lost 5 kg or more without a particular reason?",
    "(본인) B형간염 항원보유자": "Own hepatitis B surface-antigen carriage",
    "(본인) 과거병력 유무": "Own past history",
    "현재/과거 일반담배(궐련)을 피우십니까?-개비": "Cigarettes per day, current or former manufactured cigarettes",
    "과거 일반담배(궐련)을 피우십니까?-끊은지 _년": "Years since quitting manufactured cigarettes",
    "지금까지 평생 총 5갑(100개비) 이상의 담배를 피운 적이 있습니까?": "Have you smoked 5 packs (100 cigarettes) or more in your lifetime?",
    "현재 일반담배(궐련)을 피우십니까?": "Do you currently smoke manufactured cigarettes?",
    "현재/과거 일반담배(궐련)을 피우십니까?-흡연기간 총_년": "Total years smoked, manufactured cigarettes",
    "만성 염증성 대장질환(크론병, 궤양성 대장염 등)을 앓고 계시거나 과거에 앓으신 적이 있습니까? 병원에서 진단 받으신 경우만 해당됩니다.": "Do you have, or have you had, chronic inflammatory bowel disease such as Crohn's disease or ulcerative colitis? Only a diagnosis made in a hospital counts.",
    "현재/과거 궐련형 전자담배(가열담배) 피우십니까?-년": "Years using a heated tobacco product",
    "현재/과거 궐련형 전자담배(가열담배) 피우십니까?-개비": "Sticks per day, heated tobacco product",
    "과거 궐련형 전자담배(가열담배) 피우십니까?-끊은지 _년": "Years since quitting a heated tobacco product",
    "최근 한 달 동안 전자담배를 사용한 경험이 있습니까?": "Have you used an e-cigarette in the past month?",
    "현재 궐련형 전자담배(가열담배) 피우십니까?": "Do you currently use a heated tobacco product?",
    "선종성 대장용종(폴립)이나 가족성 대장용종증을 앓고 계시거나 과거에 앓으신 적이 있습니까?": "Do you have, or have you had, an adenomatous colorectal polyp or familial adenomatous polyposis?",
    "전자담배를 사용한 경험이 있습니까?": "Have you ever used an e-cigarette?",
    "지금까지 궐련형 전자담배 (가열담배, 예)아이코스, 글로, 릴 등)을 피운적 있습니까?": "Have you ever used a heated tobacco product, such as IQOS, glo, or lil?",
    "1주_20분이상 격렬한 운동": "Days per week of vigorous exercise for 20 minutes or more",
    "1주_30분이상 중간정도 운동": "Days per week of moderate exercise for 30 minutes or more",
    "1주_총30분이상 걷기 운동": "Days per week of walking totaling 30 minutes or more",
    "일주일에, 한 달에, 1년에 _번": "Times per week, per month, or per year",
    "김치를 제외하고 하루에 몇 가지 채소 (익힌 것과 날것)를 드십니까?": "Apart from kimchi, how many kinds of vegetables, cooked or raw, do you eat in a day?",
    "지난 1년간 술을 마시는 횟수는 어느 정도입니까?": "Over the past year, how often did you drink?",
    "평소 1주일간 숨이 많이 차게 만드는 고강도 신체활동을 며칠 하십니까?-주당 _일": "In a usual week, on how many days do you do vigorous activity that makes you very short of breath? Days per week",
    "평소 하루에 숨이 많이 차게 만드는 고강도 신체활동을 몇 시간 하십니까?-하루에 _시간": "On a usual day, how many hours of vigorous activity that makes you very short of breath? Hours",
    "평소 하루에 숨이 많이 차게 만드는 고강도 신체활동을 몇 시간 하십니까?-하루에 _분": "On a usual day, how many hours of vigorous activity that makes you very short of breath? Minutes",
    "일주일에 과일을 몇 번 드십니까?": "How many times a week do you eat fruit?",
    "평소 1주일간, 숨이 약간 차게 만드는 중강도 신체활동을 며칠 하십니까?-주당 _일": "In a usual week, on how many days do you do moderate activity that makes you slightly short of breath? Days per week",
    "평소 하루에 숨이 약간 차게 만드는 중강도 신체활동을 몇시간 하십니까?-하루에 _시간": "On a usual day, how long is the moderate activity that makes you slightly short of breath? Hours",
    "평소 하루에 숨이 약간 차게 만드는 중강도 신체활동을 몇 시간 하십니까?-하루에 _분": "On a usual day, how long is the moderate activity that makes you slightly short of breath? Minutes",
    "일주일에 붉은 살코기 (소고기, 돼지고기 등)를 몇 번 드십니까?": "How many times a week do you eat red meat, such as beef or pork?",
}


def _apply_stems(text: str) -> str:
    out = text
    for ko, en in _STEMS:
        if ko in out:
            out = out.replace(ko, en)
    return out


def _questionnaire(rest: str) -> str | None:
    if rest in _Q_EXACT:
        return _Q_EXACT[rest]
    m = re.match(r"술을 마시는 날은 보통 어느 정도 마십니까\?-(소주|맥주|양주|막걸리|와인) _(잔|병|캔|cc)$", rest)
    if m:
        return f"On a drinking day, how much do you usually drink? {_DRINK[m.group(1)]}, {_UNIT[m.group(2)]}"
    m = re.match(r"하루 동안 가장 많이 마셨던 음주량은 어느 정도입니까\?-(소주|맥주|양주|막걸리|와인) _(잔|병|캔|cc)$", rest)
    if m:
        return f"On the day you drank the most, how much was that? {_DRINK[m.group(1)]}, {_UNIT[m.group(2)]}"
    m = re.match(r"\(본인\) (.+) (진단여부|약물치료여부)$", rest)
    if m:
        cond, kind = m.group(1), m.group(2)
        cond_en = _apply_stems(cond)
        what = "diagnosed" if kind == "진단여부" else "treated with medication"
        if not _HANGUL.search(cond_en):
            return f"Own history: {cond_en}, {what}"
    m = re.match(r"\(가족력\)(.+)유무$", rest)
    if m:
        cond_en = _apply_stems(m.group(1))
        if not _HANGUL.search(cond_en):
            return f"Family history of {cond_en}"
    m = re.match(r"암과 관련된 검사경험 -(.+)$", rest)
    if m:
        test = _apply_stems(m.group(1).replace("유무", "").strip())
        if not _HANGUL.search(test):
            return f"Ever had this cancer-related test: {test}"
    m = re.match(r"간 질환이 있으십니까\? -(.+)$", rest)
    if m:
        cond = _apply_stems(m.group(1))
        if not _HANGUL.search(cond):
            return f"Do you have liver disease? {cond}"
    m = re.match(r"현재 또는 과거에 진단받은 (.+?)이 있으십니까\? ?-? ?(.+)$", rest)
    if not m:
        m = re.match(r"현재 또는 과거에 진단받은 (.+?)이 있으십니까\?-?(.*)$", rest)
    if m:
        organ, cond = m.group(1).strip(), m.group(2).strip()
        organ_en = _apply_stems(organ)
        cond_en = _apply_stems(cond) if cond else ""
        if not _HANGUL.search(organ_en) and not _HANGUL.search(cond_en):
            tail = f" {cond_en}" if cond_en else ""
            return f"Diagnosed now or in the past with disease of the {organ_en}?{tail}"
    m = re.match(r"현재 또는 과거에 진단받은 (.+)이 있으십니까\?-(.+)$", rest)
    if m:
        organ_en = _apply_stems(m.group(1))
        cond_en = _apply_stems(m.group(2))
        if not _HANGUL.search(organ_en) and not _HANGUL.search(cond_en):
            return f"Diagnosed now or in the past: {organ_en}, {cond_en}"
    converted = _apply_stems(rest)
    if not _HANGUL.search(converted):
        return converted
    return None


def english_name(text: str) -> str:
    """English name of a dictionary label. Falls back to the Korean text only
    when no English gloss exists; the generator checks that this does not happen
    for variable names.
    """
    from ko_glossary import EXACT

    s = " ".join(str(text).split())
    if not s:
        return ""
    if s in FULL:
        return FULL[s]
    if s in EXACT:
        return EXACT[s]
    if s in STEMS:
        return STEMS[s]
    m = re.match(r"^\[문진([0-9][0-9\-]*)\]\s*(.*)$", s)
    if m:
        rest = _questionnaire(m.group(2).strip())
        if rest:
            return f"Questionnaire {m.group(1)}: {rest}"
    converted = _apply_stems(s)
    if not _HANGUL.search(converted):
        return " ".join(converted.split())
    # Short code meanings and leftover notes still go through the glossary.
    glossed = _gloss_without_recursion(converted)
    return " ".join(glossed.split())


def _gloss_without_recursion(text: str) -> str:
    """The tail of ko_glossary.translate, without calling back into english_name."""
    from ko_glossary import EXACT, PHRASES

    if text in EXACT:
        return EXACT[text]
    out = text
    for ko, en in PHRASES:
        if ko in out:
            out = out.replace(ko, en)
    out = out.replace("[문진", "[Questionnaire ")
    out = out.replace("(본인)", "(the person)")
    out = out.replace("(가족력)", "(family history)")
    out = out.replace("(과거)", "(former)")
    out = out.replace("(현재)", "(current)")
    out = out.replace("진단여부", "whether diagnosed")
    out = out.replace("약물치료여부", "whether treated with medication")
    out = out.replace("유무", "presence")
    out = out.replace("과거병력", "past history")
    out = out.replace("조직진단", "histologic diagnosis")
    out = out.replace("종합판정", "overall judgment")
    out = out.replace("검진사업연도", "screening year")
    out = out.replace("기준연도", "reference year")
    out = out.replace("가입자구분", "insurance-status category")
    out = out.replace("실거주주소코드", "province of residence")
    out = out.replace("사망연월일", "date of death")
    out = out.replace("사망원인코드", "cause-of-death code")
    out = out.replace("최초진단연월일", "date of first diagnosis")
    out = out.replace("진단시 만나이", "age in full years at diagnosis")
    out = out.replace("성별", "sex")
    out = out.replace("요약병기", "SEER summary stage")
    out = out.replace("직접기입", "written in directly")
    return out
