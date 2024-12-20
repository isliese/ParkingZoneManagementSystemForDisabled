<h3>프로젝트명 : Parking Zone Management System For Disabled</h3>

<h3>목차</h3>

###### 1. [프로젝트 배경](#-프로젝트-배경)
###### 2. [프로젝트 목적](#-프로젝트-목적)
###### 3. [프로젝트 설명](#-프로젝트-설명)
###### 4. [프로젝트 결과](#-프로젝트-결과)
###### 5. [프로젝트 설치 및 실행 방법](#-프로젝트-설치-및-실행-방법)
###### 6. [사용 툴](#사용-툴)
###### 7. [팀원 및 참고 자료](#-팀원-및-참고-자료)
###### 8. [라이센스](#-라이센스)
###### 9. [사용 툴](#-사용-툴)

---


<h3>1. 프로젝트 배경</h3>
  
###### 최근 주차 공간이 부족해 불편하다는 이유로 장애인의 주차공간을 비장애인이 불법으로 사용하는 사례가 늘고있음. 이처럼 사회적 약자인 장애인을 위해 마련된 주차구역이지만, 일반인이 이를 악용하는 사례가 증가하면서 이러한 구역이 본래의 목적대로 수행되지 못하고 있음. 최근 사회적으로 늘어나는 장애인 전용 주차구역 악용 사례에 비해 단속 인력이 부족해 단속이 어려운 상황이며, 이 과정에서 시민 간 갈등과 행정 비효율성도 발생하고 있음.

###### 문제를 해결하기 위해서는 장애인 주차구역에 주차된 차량의 번호판을 인식하여 장애인 차량인지 확인한 후, 이를 바탕으로 과태료를 부과하거나 신고로 이어지는 체계적인 수단이 필요할 것으로 생각됨. 

---

<h3>2. 프로젝트 목적</h3>

###### - 장애인 주차 구역 침범을 실시간으로 감지하여 위반한 차량을 자동으로 신고함.
###### - 고도화된 영상 및 이미지 분석 기술을 적용하여 주차 구역 침범을 정확하게 인식하고 기록하는 시스템을 개발하는 것을 목표로 함.
###### - 장애인의 이동권을 보호, 보장하며 장애인 주차 구역의 적법한 사용을 보장하며 깨끗하고 공정한 주차 문화를 조성하는 것을 목표로 함.
###### - 장애인 주차 공간의 중요성에 대한 대중의 인식을 높이고 단속 조치를 통해 규정 준수를 장려하는 것을 목표로 함.
###### - 관리인이 장애인 주차 구역을 수동으로 순찰하고 모니터링하는 데 소요되는 시간을 줄여 주차 공간 활용을 최적화하는 것을 목표로 함
###### - 장애인 주차 공간이 필요한 사람들에게 이용 가능하고 접근 가능하도록하여 공정성과 형평성을 보장하는 것을 목표로 함.
###### - 장애인 주차 구역 침범을 실시간으로 감지하여 위반한 차량을 자동으로 신고함.


---

 <h3>3. 프로젝트 설명</h3>

######   - 장애인 주차 구역 침범을 실시간으로 감지하여 위반한 차량을 신고하는 프로그램을 개발함.
######   - 프로그램에서 장애인 주차구역에 있는 차를 선택하게 함.
######   - 그 차에 해당하는 이미지를 인공지능 모델과 연결하여 번호판을 추출함.
######   - 만약에 번호판이 등록된 장애인차량이면 장애인 차량이라는 것을 알려줌, 아니면 일반인 차량이라는 것을 알려줌.
######   - 신고페이지까지 연결하여 일반인 차량이라면 신고할 수 있도록 설계함.

---

<h3>4. 프로젝트 결과</h3>

######  UI 디자인 및 기능 노션 링크 : https://precious-pressure-b75.notion.site/445135c1ce1d46a38c780060f18c496b


---


<h3>5. 프로젝트 설치 및 실행 방법</h3>

##### [프로젝트 설치 방법] <br> 

###### OpenSourceTeamProject 파일을 다운로드하여, 파일 구조가 제대로 되어있는 지 확인한다.<br><br>
  
##### [프로젝트 실행 방법] <br>

######   이 프로그램은 실제 주차장의 각 자리마다 카메라가 설치되어 있어, 주차된 차의 번호판을 확인할 수 있음을 가정한다. 
######   이 프로그램에서는 6개의 차가 장애인 주차 구역에 주차되어있다고 가정하고, 6개의 차에 대해서 확인할 수 있도록 한다. 
######   탑재된 파일 중 app.py 파일을 실행한다. 
######   파일을 처음 실행하여, 회원가입을 진행한 후, 회원가입 한 이메일과 비밀번호로 로그인한다. 
######   확인하고 싶은 차량을 클릭하면, 해당 차량이 장애인 차량인지, 비장애인 차량인지 확인할 수 있다.
######   만약 해당 차량이 장애인 차량인 경우, 차량 이미지 오른쪽에 체크 표시가 나타난다.
######   만약 해당 차량이 비장애인 차량인 경우, 차량 이미지 오른쪽에 느낌표 표시와 함께 신고하기 버튼이 나타난다. 
######   신고하기 버튼을 누르면, "대한민국 안전 신문고 - 장애인 주차 구역 신고하기" 링크로 연결된다. 이 링크를 통해, 사용자는 장애인 주차 구역에 주차한 비장애인 차량을 신고할 수 있다.  

---

<h3>6. 사용 툴</h3>

##### [언어]
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white"> <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white"/> <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white"> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white">


##### [IDE]
<img src="https://img.shields.io/badge/Visual Studio-5C2D91?style=flat-square&logo=Visual Studio&logoColor=white"/> <img src="https://img.shields.io/badge/Figma-F24E1E?styleat-square&logo=figma&logoColor=white"/>


##### [협업 툴]
<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white"/> <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/> <img src="https://img.shields.io/badge/Kakao Talk-FFCD00?style=flat-square&logo=kakaotalk&logoColor=white"/>

---

<h3>7. 팀원 및 참고자료</h3>

###### 숙명여자대학교 인공지능공학부 23학번 김민영 <br>
###### 숙명여자대학교 인공지능공학부 23학번 김찬란 <br>
###### 숙명여자대학교 인공지능공학부 23학번 이연우 <br>
###### 숙명여자대학교 인공지능공학부 23학번 이연진 <br>


---

<h3>8. 라이센스</h3>

MIT License

Copyright (c) 2024 Minyoung Kim, Chanran kim, Yeonwoo Lee, Yeonjin Lee

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



