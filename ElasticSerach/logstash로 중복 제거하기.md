```
input {
  elasticsearch {
    hosts => "localhost"
    index => "인덱스 이름"
    query => '{"sort": ["_doc"]}'
    docinfo => true #문서의 메타데이터를 이용한다. 메타데이터를 이용하지 못하면 _index를 읽을 수 없다.
  }
}

filter {
  fingerprint {
    method => "SHA1"
    source => ["중복을 판별하는데 사용할 필드"]
    target => "[@metadata][_index]"  #생성된 fingerprint가 저장될 필드명. 이 코드에서는 _index에 저장한다.
    concatenate_sources => true #source가 동일한 데이터는 overwrite된다.
  }
}

output {
  elasticsearch {
        index => "저장할 인덱스 이름"
        document_id => "%{[@metadata][_index]}" #elasticsearch의 _index에 filter에서 생성된 fingerprint(중복 판별을 위해 생성된 값)를 사용한다.
  }
}
```
