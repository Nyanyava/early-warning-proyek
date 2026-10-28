import streamlit as st

def hitung_status(target, realisasi, sisa_hari):
    """Mengembalikan (status, deviasi, laju_minimal)."""
    deviasi = realisasi - target

    # Tentukan status proyek
    if sisa_hari <= 0 and realisasi < 100:
        status = "KRITIS"
    elif deviasi >= -5:
        status = "AMAN"
    elif deviasi >= -10:
        status = "WASPADA"
    else:
        status = "KRITIS"

    # Hitung laju progres minimal per hari
    if realisasi >= 100:
        laju = 0.0
    elif sisa_hari <= 0:
        laju = None
    else:
        laju = (100 - realisasi) / sisa_hari

    return status, deviasi, laju


st.set_page_config(page_title="Peringatan Dini Proyek", page_icon="🚦")
st.title("🚦 Peringatan Dini Keterlambatan Proyek")
st.write("Isi 3 data di bawah, status proyek akan muncul otomatis.")

target = st.number_input("Target progres saat ini (%)",
                         min_value=0.0, max_value=100.0, value=60.0, step=1.0)
realisasi = st.number_input("Realisasi progres saat ini (%)",
                            min_value=0.0, max_value=100.0, value=52.0, step=1.0)
sisa_hari = st.number_input("Sisa waktu proyek (hari)",
                            min_value=0, value=45, step=1)

status, deviasi, laju = hitung_status(target, realisasi, sisa_hari)

st.divider()

if status == "AMAN":
    st.success("🟢 AMAN: progres sesuai atau mendekati target.")
elif status == "WASPADA":
    st.warning("🟡 WASPADA: proyek mulai tertinggal, percepat pekerjaan.")
else:
    st.error("🔴 KRITIS (TERLAMBAT): tertinggal jauh, perlu tindakan segera.")

kol1, kol2 = st.columns(2)
kol1.metric("Deviasi", f"{deviasi:+.2f} %")
if laju is None:
    kol2.metric("Laju minimal", "Waktu habis")
else:
    kol2.metric("Laju minimal", f"{laju:.2f} %/hari")

st.caption("AMAN: deviasi ≥ -5% | WASPADA: -5% sampai -10% | KRITIS: < -10%")
