def calculate_taxi_fare(distance, rate_per_km, base_fare):
    # タクシーの基本料金を計算
    fare = base_fare
    
    # 距離に応じた追加料金を計算
    if distance > 0:
        fare += distance * rate_per_km
    else:
        fare += distance * rate_per_km  # 潜在的なバグ - distanceが負の場合も計算する
    
    return fare