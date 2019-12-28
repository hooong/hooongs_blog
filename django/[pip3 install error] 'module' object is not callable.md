# [pip3 install error] 'module' object is not callable

> 오늘 갑자기 `pip3 install` 을 사용해 패키지를 설치하려는데 에러가 계속 발생했었다.



- ## 발생한 에러

  ```python
  Traceback (most recent call last):
    File "/Applications/Xcode.app/Contents/Developer/usr/bin/pip3", line 10, in <module>
      sys.exit(main())
  TypeError: 'module' object is not callable
  ```

  - 이와 같은 에러를 가상환경이 켜지지 않았을때? 보았던거 같기도해서 가상환경에 문제가 있나 확인해 보았지만 그건 아니었다. 그래서 검색을 한 결과 아래와 같은 해결책을 찾았다.

  

- ## Solution

  `python3 -m pip uninstall pip` 를 터미널에 쳐서 pip를 uninstall하는 거였다. 

  - 이렇게하니 마법같이 에러가 발생하지 않았다.
  - 설명을 보니 운영체제에서 제공하는 global pip와 user의 specific한 pip간의 conflict가 발생하는거라고 한다.