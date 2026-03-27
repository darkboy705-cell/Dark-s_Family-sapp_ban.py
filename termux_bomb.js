const { Client, LocalAuth } = require('whatsapp-web.js');

const client = new Client({
    authStrategy: new LocalAuth(),
    puppeteer: { args: ['--no-sandbox'], headless: true }
});

client.on('code', (code) => {
    console.log('\n-------------------------------------------');
    console.log('VOTRE CODE DE LIAISON : ' + code);
    console.log('-------------------------------------------');
    console.log('Allez dans WhatsApp > Appareils liés > Lier avec numéro.\n');
});

client.on('ready', () => { console.log('✅ Connecté ! Prêt pour le bombing.'); });

client.initialize();
