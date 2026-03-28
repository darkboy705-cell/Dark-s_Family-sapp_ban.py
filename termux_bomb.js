const { default: makeWASocket, useMultiFileAuthState, fetchLatestBaileysVersion, delay } = require("@whiskeysockets/baileys");
const pino = require("pino");
const readline = require("readline");

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const question = (text) => new Promise((resolve) => rl.question(text, resolve));

async function startBot() {
    const { state, saveCreds } = await useMultiFileAuthState('auth_info');
    const { version } = await fetchLatestBaileysVersion();

    const sock = makeWASocket({
        version,
        auth: state,
        logger: pino({ level: 'silent' }),
        printQRInTerminal: false
    });

    if (!sock.authState.creds.registered) {
        console.log("\n--- CONNEXION SANS QR CODE ---");
        const phoneNumber = await question("Entre ton numéro avec l'indicatif (ex: 5093xxxxxxx) : ");
        
        // Attendre un court instant avant de demander le code
        await delay(3000);
        const code = await sock.requestPairingCode(phoneNumber.trim());
        
        console.log(`\nTON CODE DE JUMELAGE : \x1b[32m${code}\x1b[0m`);
        console.log("Instructions : WhatsApp > Appareils connectés > Lier avec un numéro de téléphone.\n");
    }

    sock.ev.on('creds.update', saveCreds);

    sock.ev.on('connection.update', (update) => {
        const { connection } = update;
        if (connection === 'open') {
            console.log("\n✅ Outil opérationnel et connecté !");
        } else if (connection === 'close') {
            startBot();
        }
    });

    // Exemple de puissance : Répondre au mot "menu"
    sock.ev.on('messages.upsert', async ({ messages }) => {
        const m = messages[0];
        if (!m.message || m.key.fromMe) return;
        const text = m.message.conversation || m.message.extendedTextMessage?.text;

        if (text?.toLowerCase() === 'menu') {
            await sock.sendMessage(m.key.remoteJid, { text: 'Bot actif. En attente de vos commandes...' });
        }
    });
}

startBot();

