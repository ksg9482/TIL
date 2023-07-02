### CharField
* 문자열을 저장할 때 사용한다.
* 길이 제한 문자열을 삽입 한다.(max_length=100) 

### EmailField
* 이메일 주소 형태를 저장할 때 사용한다.
* 길이 제한 문자열을 삽입 한다.(max_length=100) 

### URLField
* URL 주소 형태를 저장할 때 사용한다.

### TextField
* CharField와 유사하지만, 더욱 대용량의 문자열을 처리 한다.
* DB용량을 더 소모하지만 굳이 크기 제한을 하지 않는다.

### IntegerField
* 32비트 정수형 필드 이며 정수 사이즈에 따라 다른 필드를 사용할 수 있다.
  * BigIntegerField 
  * SmallIntegerField
* default를 통해 수정이 없을 경우 지정된 값을 자동으로 저장한다.

### BooleanField
* True 또는 False를 저장하고, DB상에서는 0, 1로 저장되는 SmallIntegerField형식이다.
* Null을 허용하려면 NullBooleanField를 사용한다.
* initial을 통해 수정이 없을 경우 지정된 값을 자동으로 저장한다.

### DatetimeField
* 시간과 관련된 값을 저장한다.
  * DateField: 날짜만 저장하고 싶을 때 사용
  * TimeField: 시간만 저장하고 싶을 때 사용

### DecimalField
* 소수점 관련 필드를 말한다.
* max_digits와 decimal_place를 지정해야 하고, 지정한 값으로 저장하려는 숫자가 지정한 포맷에 맞는지 확인 가능하다.

### FileField
* 파일을 업로드 한다.
* upload_to 옵션에 해당 경로를 지정해야 한다.
* 폴더 탐색은 settings.py에서 설정한 MEDIA_ROOT부터 시작한다.

### ImageField
* FileField의 파생이다.
* 해당 파일이 이미지인지 확인 가능하다.
