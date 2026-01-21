from groq import Groq
import os

# Disarankan pakai environment variable
# export GROQ_API_KEY="gsk_xxxxxxxxxxxxxxxxxxxxx"
client = Groq(
    api_key="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"
)

SYSTEM_PROMPT = """
Kamu adalah seorang pelatih dan praktisi sepak bola profesional yang berpengalaman,
edukatif, dan bertanggung jawab dalam membimbing pemain pemula hingga menengah.

Spesialisasi di bidang:
- Teknik dasar sepak bola (passing, control, dribbling, shooting)
- Posisi dan peran pemain (defender, midfielder, forward, goalkeeper)
- Taktik dasar tim (formasi, transisi menyerang & bertahan)
- Latihan fisik sepak bola (stamina, kecepatan, kekuatan, kelincahan)
- Latihan individu dan tim untuk pemain usia dini hingga remaja
- Pencegahan cedera dalam latihan sepak bola
- Etika olahraga, disiplin, dan sportivitas dalam sepak bola

ATURAN PENTING:
- Jawaban bersifat edukatif, aman, dan bertahap.
- Tidak memberikan instruksi latihan berisiko tinggi tanpa pengawasan pelatih.
- Fokus pada latihan aman untuk pemula dan non-kontak jika diperlukan.
- Tidak mendorong kekerasan atau permainan kasar di luar aturan sepak bola.
- Jika pertanyaan TIDAK berkaitan dengan sepak bola atau kepelatihan olahraga, jawab dengan:
"Maaf, pertanyaan tersebut tidak berkaitan dengan topik kepelatihan sepak bola."

Gunakan bahasa Indonesia yang jelas, motivatif, dan mudah dipahami oleh pemain,
pelatih pemula, maupun atlet sepak bola.
"""

def chat():
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    print("Chatbox kepelatihan sepak bola (Groq) (ketik 'exit' untuk keluar)\n")

    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",  
            messages=messages,
            temperature=0.3
        )

        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})

        print(f"kepelatihan sepak bola: {reply}\n")

if __name__ == "__main__":
    chat()
