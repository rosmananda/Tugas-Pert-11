<?php
function otp_encrypt($plaintext, $key) {
    $ciphertext = "";
    $plaintextLength = strlen($plaintext);

    for ($i = 0; $i < $plaintextLength; $i++) {
        $result = ord($plaintext[$i]) ^ ord($key[$i]);
        $ciphertext .= chr($result);
    }

    return $ciphertext;
}

function otp_decrypt($ciphertext, $key) {
    $decrypted_text = "";
    $ciphertextLength = strlen($ciphertext);

    for ($i = 0; $i < $ciphertextLength; $i++) {
        $result = ord($ciphertext[$i]) ^ ord($key[$i]);
        $decrypted_text .= chr($result);
    }

    return $decrypted_text;
}

// Contoh penggunaan
$plaintext = "RUSDI";
$key = "CRUSH";

// Enkripsi
$hasil_enkripsi = otp_encrypt($plaintext, $key);
echo "Plainteks: $plaintext\n";
echo "Kunci: $key\n";
echo "Hasil Enkripsi: $hasil_enkripsi\n";

// Dekripsi
$hasil_dekripsi = otp_decrypt($hasil_enkripsi, $key);
echo "Hasil Dekripsi: $hasil_dekripsi\n";
?>
