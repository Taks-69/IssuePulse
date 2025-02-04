// Use discord.js version 14.7.1 | npm install discord.js@14.7.1
const { Client, GatewayIntentBits } = require('discord.js');
const axios = require('axios');

// Remplace par ton token Discord
const DISCORD_BOT_TOKEN = "YOUR_DISCORD_BOT_TOKEN";

// Remplace par les infos de ton dépôt GitHub
const GITHUB_OWNER = "YOUR_GITHUB_USERNAME";
const GITHUB_REPO = "YOUR_GITHUB_REPOSITORY";

const CHANNEL_ID_DIDI = "ID_CHANNEL_DISCORD";

// Variables pour stocker le dernier numéro d'issue et de PR
let lastIssueNumber = 0;
let lastPrNumber = 0;

const client = new Client({ intents: [GatewayIntentBits.Guilds] });

async function checkUpdates(channel) {
    const issuesUrl = `https://api.github.com/repos/${GITHUB_OWNER}/${GITHUB_REPO}/issues`;

    try {
        const response = await axios.get(issuesUrl, { timeout: 10000 });
        const issues = response.data;

        for (const issue of issues) {
            if (!issue.pull_request) {
                // C'est une issue
                if (issue.number > lastIssueNumber) {
                    channel.send(`Nouvelle issue #${issue.number}: **${issue.title}**\n${issue.html_url}`);
                    lastIssueNumber = issue.number;
                }
            } else {
                // C'est un pull request
                if (issue.number > lastPrNumber) {
                    channel.send(`Nouveau pull request #${issue.number}: **${issue.title}**\n${issue.html_url}`);
                    lastPrNumber = issue.number;
                }
            }
        }
    } catch (error) {
        console.error("Erreur lors de la récupération des données GitHub:", error.message);
    }
}

client.once('ready', () => {
    console.log(`Connecté en tant que ${client.user.tag}!`);
    // Remplace "YOUR_CHANNEL_ID" par l'ID du salon où envoyer les alertes
    const channel = client.channels.cache.get(CHANNEL_ID_DIDI);
    if (!channel) {
        console.error("Salon introuvable, vérifie l'ID du salon.");
        return;
    }

    // Vérifie toutes les 60 secondes
    setInterval(() => {
        checkUpdates(channel);
    }, 60 * 1000);
});

client.login(DISCORD_BOT_TOKEN);
