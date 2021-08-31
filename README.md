# 온라인 도서관(레이서 도서관) 소개

## **1. 프로젝트 소개**

> **온라인으로 도서 내여와 반납을 관리할 수 있는 '책 대여 웹 서비스'**

👉 책 정보와 대여상태를 제공하여 사용자들이 원하는 책을 자유롭게 대여하고 반납할 수 있는 서비스 제공합니다.

**🚀 기술 스택**
|구분|설명|
|:---:|:----------:|
|Front|HTML, jinja2, CSS|
|Server|Flask|
|DB|SQLite, SQLAlchemy|

## **2. 프로젝트 목표**

- 책 정보를 제공하고 리뷰와 평점을 통해 사용자가 원하는 책을 빌리고 반납할 수 있게 만든다.

## **3. 기능**

`로그인 / 회원가입`

- 사용자로부터 아이디와 비밀번호를 입력받아 로그인
- 로그인한 유저에 대해 session으로 관리
- 비밀번호는 영문, 숫자, 특수문자를 조합하여 최소 8자리 이상 또는 영문, 숫자, 특수문자 중 2종류 이상을 조합하여 10자리 이상의 길이로 구성

`메인`

- 현재 DB상에 존재하는 모든 책의 정보를 가져온다.
- 현재 DB상에 남아있는 책의 수 표기
- 책 사진 및 이름 클릭시 해당 책 페이지로 이동
- 평점은 DB상에 담겨 있는 책의 평점의 평균으로 표기 👉 여러 사용자들이 남긴 리뷰 상의 평점 평균 적용
- 페이지네이션 👉 한 페이지당 8권의 책 표기

➕ 검색 기능 👉 원하는 책 제목 통해 책을 검색할 수 있음

`대여 / 반납`

- 메인 페이지의 대여하기 버튼을 클릭하여 대여
- 남은 책이 없을 경우 대여 불가
- 대여중인 책은 같은 사용자가 또 다시 대여할 수 없음
- 반납페이지에서는 대여한 모든 책을 표기
- 반납하기 버튼을 클릭하여 반납
- 대여기록에는 '반납한 내역이 있는' 책만 조회 가능

➕ 검색 기능 👉 원하는 책 제목 통해 책을 검색할 수 있음

`책소개 / 리뷰`

- 책의 저자와 출판사 등 정보 표기
- 댓글 기능. 최신 댓글이 보이도록 sorting
- 댓글 작성 시 1점 단위로 평점 입력
- 작성한 댓글 삭제 기능

`관리자 페이지`

- 관리자 로그인
- 새 책 등록하기
- 등록 내역 확인

## **4. 데이터베이스 구조**

|   구분    |                             설명                             |            목적            |
| :-------: | :----------------------------------------------------------: | :------------------------: |
|   User    |              유저의 아이디, 패스워드, 이름 저장              |       회원 정보 저장       |
|   Book    |     책 이름, 출판사, 작가 등 세부 정보와 평점, 재고 저장     |        책 정보 저장        |
|  Rental   |         대여일, 반납일, 책 아이디, 유저 아이디 저장          |       대여 정보 저장       |
|  Comment  | 리뷰 내용, 평점, 작성일, 수정일, 유저 아이디, 책 아이디 저장 |       리뷰 정보 저장       |
| UserRoles |                 유저 아이디, 권한 정보 저장                  |      관리자 권한 부여      |
| AddStock  |       추가한 재고에 대한 날짜, isbn, 유저 아이디 저장        | 추가 재고에 대한 정보 저장 |

![EliceLibrary.png](./erd.png)
