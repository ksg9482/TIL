# Jest설정
### package.json
```javascript
"jest": {
    "moduleNameMapper": {
      "^src/(.*)$": "<rootDir>/$1"
    },
    "moduleFileExtensions": [
      "js",
      "json",
      "ts"
    ],
    "rootDir": "src",
    "testRegex": ".*\\.spec\\.ts$",
    "transform": {
      "^.+\\.(t|j)s$": "ts-jest"
    },
    "collectCoverageFrom": [
      "**/*.service.(t|j)s"
    ],
    "coverageDirectory": "../coverage",
    "testEnvironment": "node",
    "coveragePathIgnorePatterns": [
      "node_modules",
      ".entity.ts",
      ".constants.ts"
    ]
  }
```

### 테스트 폴더 내부
jest-e2e.json
```javascript
{
  "moduleFileExtensions": ["js", "json", "ts"],
  "rootDir": ".",
  "testEnvironment": "node",
  "testRegex": ".e2e-spec.ts$",
  "transform": {
    "^.+\\.(t|j)s$": "ts-jest"
  },
  "moduleNameMapper": {
    "^src/(.*)$":"<rootDir>/../src/$1"
    
  }
}

```
