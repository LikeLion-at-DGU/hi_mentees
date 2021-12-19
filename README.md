<img src="https://img.shields.io/badge/python-blue?style=뱃지모양&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Django-lightcoral?style=뱃지모양&logo=Django&logoColor=white"/>

# hi_mentees


![image](https://user-images.githubusercontent.com/81295661/146660198-b84f07f3-f5b5-4340-8013-72320f1a490c.png)

---

## 서비스 목표

▪ 동국대학교 HI-SW 봉사단의 비대면 봉사활동을 위한 온라인 멘토멘티 컨택 웹사이트입니다 :) <br>
▪ 인터넷 강의 사이트와 비슷한 화면 구성으로 멘토가 직접 강의를 등록할 수 있고 멘티는 이러한 강좌를 수강신청 할 수 있습니다. <br>
▪ 강의 후기, 강사에 대한 후기를 남길 수 있습니다. <br>
▪ IT에 관심이 있는 중학생, 고등학생들이 해당 사이트 Q&A 카테고리에서 관련 질문을하고 대학생 멘토들은 이에 대해 답변을 달아 줄 수 있습니다. <br>
<br>
👍  누적 봉사시간 조회 가능 <br>
👍  수강 내역 조회 가능<br>
👍  QnA 기능<br>
👍  수요에 따른 강의 개설 가능<br>
👍  강사 및 강의 후기 조회 가능(보다 주체적인 선택이 가능)



<br>

## 서비스 내용
### **화면 실행**

```python
pip install -r requirements.txt
python manage.py runserver
```

<br>

### superuser 등록
- 사이트의 관리자는 superuser를 이용해 등록이 가능합니다.
``` python
python manage.py createsuperuser
```
- admin 페이지에서 회원관리 및 수강 승인이 가능합니다.
- User 프로필에서 ADMIN APPROVED 수정을 통해 학생의 회원가입을 승인할 수 있습니다.
 
<br>


### **회원가입 및 로그인**
![image](https://user-images.githubusercontent.com/81295661/146660383-f7d1c7b3-810d-41ba-8a44-6ee3a3db5a52.png)
- 프로필은 강사와 학생으로 나눠집니다.

<br>


### **메인페이지**
![image](https://user-images.githubusercontent.com/81295661/146660445-a4e59877-9b0a-401f-a653-fb6fc453d594.png)

<br>

### **소개페이지**
![image](https://user-images.githubusercontent.com/81295661/146660451-d22c93ba-b04e-4895-a5b3-7ea4601d3a1f.png)

<br>

### **강의페이지**
![image](https://user-images.githubusercontent.com/81295661/146660460-0327a2c9-e85d-4a0e-923d-8cb5cdb17dfd.png)

<br>

### **강의 상세페이지**
![image](https://user-images.githubusercontent.com/81295661/146660472-51aece95-a6fc-45fa-a40d-f0e71ba5e978.png)
![image](https://user-images.githubusercontent.com/81295661/146660477-204f410b-b33b-4ebe-9f75-86b960dd8950.png)
![image](https://user-images.githubusercontent.com/81295661/146660480-c3305c2c-c1fb-4d98-b03e-d0c963df4105.png)
![image](https://user-images.githubusercontent.com/81295661/146660483-1c93cb9d-a808-4ed4-b217-8a7b67123398.png)
![image](https://user-images.githubusercontent.com/81295661/146660489-74883740-b12f-41a3-93a5-cab17a852250.png)

<br>

### **마이페이지**
![image](https://user-images.githubusercontent.com/81295661/146660505-4454ea7c-c0f3-47e7-b8e3-3adafabcd885.png)
![image](https://user-images.githubusercontent.com/81295661/146660509-500b119a-bb67-436a-8d71-d4ceec704421.png)

<br>

### **강사 마이페이지**
![image](https://user-images.githubusercontent.com/81295661/146660515-17061395-43cc-49a5-872f-ed84594cf901.png)

<br>

### **후기 작성**
![image](https://user-images.githubusercontent.com/81295661/146660525-20f45bae-1f01-487f-bf58-76915b0bd62d.png)
![image](https://user-images.githubusercontent.com/81295661/146660530-718d5950-d620-4def-a448-4a37fc11e55d.png)

<br>

## **강의 후기**
![image](https://user-images.githubusercontent.com/81295661/146660539-a684ed18-611b-444a-859a-4f9f41816f0c.png)
![image](https://user-images.githubusercontent.com/81295661/146660554-39bfc8ac-5fae-4194-aa4f-e5e0170021eb.png)

<br>

## **질의응답**
![image](https://user-images.githubusercontent.com/81295661/146660549-67721450-8a25-47d5-bcab-4408654f5838.png)
![image](https://user-images.githubusercontent.com/81295661/146660550-cac31cb0-d5f2-4b29-8469-d5d13d439a3d.png)




<br>



## 구현 내용

- 강사, 학생의 구분을 통한 회원 관리
- 수강신청 및 좋아요 기능 구현
- 강의 후기 및 질의응답 기능 구현
- 마이페이지 기능 구현
- 각종 기능에 대한 CRUD 구현
- Bootstrap을 이용한 화면 구성
