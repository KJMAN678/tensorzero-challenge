# TensorZero Django デモアプリケーション

TensorZero - 工業グレードのLLMアプリケーションのためのオープンソーススタックのデモアプリケーションです。

## 概要

このDjangoアプリケーションは、TensorZeroライブラリの主要機能を紹介します：

- 🚀 **統合APIゲートウェイ** - 複数のLLMプロバイダーへの統一されたインターフェース
- 📊 **観測性とモニタリング** - 推論の追跡と分析
- 🔧 **最適化** - プロンプトエンジニアリングとモデルファインチューニング
- 🧪 **評価と実験** - A/Bテストとモデル比較
- ⚡ **高性能** - Rustで構築され、<1ms p99レイテンシー

## 機能

1. **推論デモ** - 単一モデルでの推論実行
2. **モデル比較** - 複数モデルの応答を並べて比較
3. **フィードバックシステム** - 推論結果の評価と追跡
4. **分析ダッシュボード** - 使用状況とパフォーマンスの洞察
5. **日本語インターフェース** - 完全な日本語対応

## セットアップ

### 必要条件
- Python 3.8以上
- Django 5.1以上
- TensorZero 2025.6.3以上

### インストール

1. リポジトリをクローン：
```bash
git clone <repository-url>
cd tensorzero_django_demo
```

2. 仮想環境を作成して有効化：
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# または
venv\Scripts\activate  # Windows
```

3. 依存関係をインストール：
```bash
pip install -r requirements.txt
```

4. データベースをマイグレート：
```bash
python manage.py migrate
```

5. スーパーユーザーを作成（管理画面用）：
```bash
python manage.py createsuperuser
```

6. 開発サーバーを起動：
```bash
python manage.py runserver
```

7. ブラウザで http://localhost:8000 にアクセス

## TensorZero Gatewayの設定

実際のTensorZero機能を使用するには：

1. TensorZero Gatewayをデプロイ
2. モデルプロバイダーを設定（OpenAI、Anthropic等）
3. `views.py`のGATEWAY_URLを更新
4. シミュレーションコードを実際のTensorZeroクライアント呼び出しに置き換え

## プロジェクト構造

```
tensorzero_django_demo/
├── tensorzero_demo/          # Djangoプロジェクト設定
├── tensorzero_showcase/      # メインアプリケーション
│   ├── models.py            # データモデル
│   ├── views.py             # ビューロジック
│   ├── urls.py              # URLルーティング
│   ├── admin.py             # 管理画面設定
│   └── templates/           # HTMLテンプレート
│       └── tensorzero_showcase/
│           ├── base.html
│           ├── index.html
│           ├── inference_demo.html
│           ├── model_comparison.html
│           ├── inference_detail.html
│           ├── comparison_detail.html
│           └── analytics.html
├── manage.py
├── requirements.txt
└── README.md
```

## 使用方法

### 推論デモ
1. 「推論デモ」ページにアクセス
2. モデルを選択
3. プロンプトを入力
4. パラメータを調整（Temperature、最大トークン数）
5. 「推論を実行」をクリック

### モデル比較
1. 「モデル比較」ページにアクセス
2. 比較したいモデルを複数選択
3. 共通のプロンプトを入力
4. 「モデルを比較」をクリック
5. 結果を並べて比較

### フィードバック
- 各推論結果に評価を付けることができます
- 評価指標：品質、関連性、一貫性、有用性

### 分析
- 「分析」ページで使用状況とパフォーマンスを確認
- モデル別の使用率、応答時間、評価を表示

## 注意事項

現在のバージョンは**シミュレーション**モードで動作します。実際のLLM応答を得るには：

1. TensorZero Gatewayをデプロイ
2. APIキーを設定
3. `views.py`のコードを更新

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 貢献

プルリクエストを歓迎します！大きな変更の場合は、まずissueを作成して変更内容を議論してください。

## サポート

問題が発生した場合は、GitHubのissueを作成してください。