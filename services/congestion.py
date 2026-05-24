def analyze_congestion(count_per_kelas):
    total_smp = (count_per_kelas.get('Motorcycle', 0) * 0.5) + \
                (count_per_kelas.get('Car', 0) * 1.0) + \
                (count_per_kelas.get('Bus', 0) * 1.3) + \
                (count_per_kelas.get('Truck', 0) * 1.3)
                
    if total_smp >= 25:
        status = "MACET"
    elif total_smp >= 15:
        status = "PADAT"
    else:
        status = "LANCAR"
        
    return {
        "status": status,
        "total_smp": round(total_smp, 1)
    }