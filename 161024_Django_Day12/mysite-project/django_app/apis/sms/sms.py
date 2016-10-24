"""
발신번호 : 010-2995-3874
1. Python SDK를 이용해서 SMS전송 테스트를 해본다
    1-1. pip로 SDK 패키지 설치
    1-2. 테스트할 파이썬 파일 작성 (send_sms_test.py)
    1-3. API Key, API Secret Key값 대입
    1-4. 발신번호에 위 번호 사용
    1-5. 수신번호에 자신의 번호 사용
    1-6. 보내보자!
2. 테스트에 성공한 후, sms전송 API를 apis/sms/sms.py안에 구현해본다 (send_sms함수)
    2-1. 내용/수신자번호를 받도록 구현
3. Member모델에 전화번호 필드를 추가, Shell통해서 해당 User의 전화번호를 추가
    3-1. 필드추가
    3-2. migration
    3-3. Shell에서 user의 전화번호필드 내용 추가 후 save()
    3-4(extra). User save시, 전화번호필드에 '-'기호 넣었을 경우 삭제한 후 저장
4. signal또는 Model의 save메서드 오버라이드로 댓글이 달릴 시 간단한 알림을 보내본다
    4-1. 전화번호 필드가 비었을 경우, 보내지않도록한다
"""