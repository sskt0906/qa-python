\# Python API Test Automation Practice



Python、pytest、requestsを使ったAPIテスト自動化の練習プロジェクトです。



\## 概要



このプロジェクトでは、テスト用APIサービスである httpbin を対象に、APIの正常系・異常系テストを自動化しています。



pytestを使ってテストを実行し、requestsを使ってAPIへリクエストを送信しています。



\## 使用技術



\* Python

\* pytest

\* requests

\* pytest-html



\## テスト対象



\* https://httpbin.org



\## 実装しているテスト



| No | テスト関数                             | テスト内容                  | 期待結果             |

| -- | --------------------------------- | ---------------------- | ---------------- |

| 1  | test\_get\_api\_status\_code          | GET APIにアクセスする         | ステータスコード200が返る   |

| 2  | test\_get\_api\_json                 | GET APIのJSONレスポンスを確認する | url項目が含まれる       |

| 3  | test\_post\_api\_json                | JSONデータをPOST送信する       | 送信した値がレスポンスに含まれる |

| 4  | test\_not\_found\_status\_code        | 404用URLにアクセスする         | ステータスコード404が返る   |

| 5  | test\_server\_error\_status\_code     | 500用URLにアクセスする         | ステータスコード500が返る   |

| 6  | test\_status\_code\_parametrize\[200] | parametrizeで200を確認する   | ステータスコード200が返る   |

| 7  | test\_status\_code\_parametrize\[404] | parametrizeで404を確認する   | ステータスコード404が返る   |

| 8  | test\_status\_code\_parametrize\[500] | parametrizeで500を確認する   | ステータスコード500が返る   |



\## セットアップ



必要なライブラリをインストールします。



```bash

python -m pip install pytest requests pytest-html

```



\## テスト実行方法



通常実行:



```bash

python -m pytest

```



詳細表示:



```bash

python -m pytest -v

```



\## HTMLレポートの出力



テスト結果をHTMLレポートとして出力する場合は、以下のコマンドを実行します。



```bash

python -m pytest -v --html=report.html --self-contained-html

```



出力された `report.html` をブラウザで開くと、テスト結果を確認できます。



Windows PowerShellの場合:



```powershell

start report.html

```



\## 学習した内容



このプロジェクトを通して、以下を学習しました。



\* pytestによるテスト実行

\* requestsによるGETリクエスト

\* requestsによるPOSTリクエスト

\* ステータスコードの確認

\* JSONレスポンスの確認

\* 正常系テスト

\* 異常系テスト

\* pytest.mark.parametrizeによるパラメータ化テスト

\* pytest-htmlによるHTMLレポート出力



\## 実行結果例



```text

test\_api.py::test\_get\_api\_status\_code PASSED

test\_api.py::test\_get\_api\_json PASSED

test\_api.py::test\_post\_api\_json PASSED

test\_api.py::test\_not\_found\_status\_code PASSED

test\_api.py::test\_server\_error\_status\_code PASSED

test\_api.py::test\_status\_code\_parametrize\[200] PASSED

test\_api.py::test\_status\_code\_parametrize\[404] PASSED

test\_api.py::test\_status\_code\_parametrize\[500] PASSED

```



\## 目的



APIテスト自動化の基本を理解し、QAエンジニアとして必要なテスト設計・自動化・実行結果確認の流れを身につけることを目的としています。

\# Python API Test Automation Practice



Python、pytest、requestsを使ったAPIテスト自動化の練習プロジェクトです。



\## 概要



このプロジェクトでは、テスト用APIサービスである httpbin を対象に、APIの正常系・異常系テストを自動化しています。



pytestを使ってテストを実行し、requestsを使ってAPIへリクエストを送信しています。



\## 使用技術



\* Python

\* pytest

\* requests

\* pytest-html



\## テスト対象



\* https://httpbin.org



\## 実装しているテスト



| No | テスト関数                             | テスト内容                  | 期待結果             |

| -- | --------------------------------- | ---------------------- | ---------------- |

| 1  | test\_get\_api\_status\_code          | GET APIにアクセスする         | ステータスコード200が返る   |

| 2  | test\_get\_api\_json                 | GET APIのJSONレスポンスを確認する | url項目が含まれる       |

| 3  | test\_post\_api\_json                | JSONデータをPOST送信する       | 送信した値がレスポンスに含まれる |

| 4  | test\_not\_found\_status\_code        | 404用URLにアクセスする         | ステータスコード404が返る   |

| 5  | test\_server\_error\_status\_code     | 500用URLにアクセスする         | ステータスコード500が返る   |

| 6  | test\_status\_code\_parametrize\[200] | parametrizeで200を確認する   | ステータスコード200が返る   |

| 7  | test\_status\_code\_parametrize\[404] | parametrizeで404を確認する   | ステータスコード404が返る   |

| 8  | test\_status\_code\_parametrize\[500] | parametrizeで500を確認する   | ステータスコード500が返る   |



\## セットアップ



必要なライブラリをインストールします。



```bash

python -m pip install pytest requests pytest-html

```



\## テスト実行方法



通常実行:



```bash

python -m pytest

```



詳細表示:



```bash

python -m pytest -v

```



\## HTMLレポートの出力



テスト結果をHTMLレポートとして出力する場合は、以下のコマンドを実行します。



```bash

python -m pytest -v --html=report.html --self-contained-html

```



出力された `report.html` をブラウザで開くと、テスト結果を確認できます。



Windows PowerShellの場合:



```powershell

start report.html

```



\## 学習した内容



このプロジェクトを通して、以下を学習しました。



\* pytestによるテスト実行

\* requestsによるGETリクエスト

\* requestsによるPOSTリクエスト

\* ステータスコードの確認

\* JSONレスポンスの確認

\* 正常系テスト

\* 異常系テスト

\* pytest.mark.parametrizeによるパラメータ化テスト

\* pytest-htmlによるHTMLレポート出力



\## 実行結果例



```text

test\_api.py::test\_get\_api\_status\_code PASSED

test\_api.py::test\_get\_api\_json PASSED

test\_api.py::test\_post\_api\_json PASSED

test\_api.py::test\_not\_found\_status\_code PASSED

test\_api.py::test\_server\_error\_status\_code PASSED

test\_api.py::test\_status\_code\_parametrize\[200] PASSED

test\_api.py::test\_status\_code\_parametrize\[404] PASSED

test\_api.py::test\_status\_code\_parametrize\[500] PASSED

```



\## 目的



APIテスト自動化の基本を理解し、QAエンジニアとして必要なテスト設計・自動化・実行結果確認の流れを身につけることを目的としています。



