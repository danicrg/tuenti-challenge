function chr() {
    printf \\$(printf '%03o' $1)
}

function hex() {
    printf '%02X\n' $1
}

function dec() {
    printf $(( 16#$1 ))
}

function encrypt() {
    key=$1
    msg=$2
    crpt_msg=""
    for ((i=0; i<${#msg}; i++)); do
        c=${msg:$i:1}
        asc_chr=$(echo -ne "$c" | od -An -tuC)
        key_pos=$((${#key} - 1 - i))
        key_char=${key:$key_pos:1}
        crpt_chr=$(( $asc_chr ^ ${key_char} ))
        hx_crpt_chr=$(hex $crpt_chr)
        crpt_msg=${crpt_msg}${hx_crpt_chr}
    done
    echo $crpt_msg
}

function get_key() {
    msg=$1
    crpt_msg=$2
    key=""
    for ((i=${#msg}-1; i>-1; i--)); do
        c=${msg:$i:1}
        ec=${crpt_msg:$i*2:2}
        asc_chr=$(echo -ne "$c" | od -An -tuC)
        dc_crpt_chr=$(dec $ec)
        key_chr=$(( $asc_chr ^ ${dc_crpt_chr} ))
        key=${key}${key_chr}
        
    done
    echo $key
}

function decrypt() {
    key=$1
    crpt_msg=$2
    msg=""
    for ((i=0; i<${#key}; i++)); do
        key_pos=$((${#key} - 1 - ${i}))
        key_char=${key:$key_pos:1}
        ec=${crpt_msg:$i*2:2}
        dc_crpt_chr=$(dec $ec)
        asc_chr=$(( $key_char ^ ${dc_crpt_chr} ))
        msg_char=$(chr $asc_chr)
        msg=${msg}${msg_char}

    done
    echo $msg
}


knownInput="514;248;980;347;145;332"
knownOutput="3633363A33353B393038383C363236333635313A353336"
unknOutput="3A3A333A333137393D39313C3C3634333431353A37363D"

key=$(get_key $knownInput $knownOutput)

decrypt $key $unknOutput > flag.txt

