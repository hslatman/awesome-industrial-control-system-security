# awesome-industrial-control-system-security
A curated list of resources related to Industrial Control System (ICS) security.

Feel free to [contribute](CONTRIBUTING.md).


## Tools

<table>
    <tr>
        <td>
            <a href="https://cset.inl.gov/SitePages/Home.aspx" target="_blank">CSET</a>
        </td>
        <td>
            The Cyber Security Evaluation Tool (CSET®) assists organizations in protecting their key national cyber assets. 
            This tool provides users with a systematic and repeatable approach for assessing the security posture of their cyber systems and networks. 
            It includes both high-level and detailed questions related to all industrial control and IT systems.​
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://www.digitalbond.com/tools/basecamp/3s-codesys/" target="_blank">Digital Bond's 3S CoDeSys Tools</a>
        </td>
        <td>
            Digital Bond created three tools for interacting with PLCs that run CoDeSys, consisting of a command shell, file transfer and NMap script.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://github.com/digitalbond/Redpoint" target="_blank">Digital Bond's ICS Enumeration Tools</a>
        </td>
        <td>
            Redpoint is a Digital Bond research project to enumerate ICS applications and devices using nmap extensions.
            It can be used during assessments to discover ICS devices and pull information that would be helpful in secondary testing. 
            The Redpoint tools use legitimate protocol or application commands to discover and enumerate devices and applications. 
            There is no effort to exploit or crash anything, but be wise and careful.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://github.com/iadgov/GRASSMARLIN" target="_blank">GRASSMARLIN</a>
        </td>
        <td>
            GRASSMARLIN provides IP network situational awareness of industrial control systems (ICS) and Supervisory Control and Data Acquisition (SCADA) networks to support network security. Passively map, and visually display, an ICS/SCADA network topology while safely conducting device discovery, accounting, and reporting on these critical cyber-physical systems.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://github.com/sourceperl/mbtget" target="_blank">mbtget</a>
        </td>
        <td>
            mbtget - Simple perl script for make some modbus transaction from the command line.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://github.com/scy-phy/minicps" target="_blank">MiniCPS</a>
        </td>
        <td>
            MiniCPS: A toolkit for security research on Cyber-Physical
            Systems from Singapore University of Technology and Design (SUTD).
        </td>
    </tr>
    <tr>
        <td>
            <a href="https://github.com/enddo/smod" target="_blank">MODBUS Penetration Testing Framework</a>
        </td>
        <td>
            smod is a modular framework with every kind of diagnostic and offensive feature you could need in order to pentest modbus protocol. It is a full Modbus protocol implementation using Python and Scapy. The framework can be used to perform vulnerability assessments.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="http://modbuspal.sourceforge.net/" target="_blank">ModbusPal</a>
        </td>
        <td>
            ModbusPal is a MODBUS slave simulator. Its purpose is to offer an easy to use interface with the capabilities to reproduce complex and realistic MODBUS environments.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://github.com/moki-ics/modscan" target="_blank">ModScan</a>
        </td>
        <td>
            ModScan is a new tool designed to map a SCADA MODBUS TCP based network.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://sourceforge.net/projects/nettoplcsim/" target="_blank">NetToPLCSim</a>
        </td>
        <td>
            TCP/IP-Network extension for the PLC simulation software Siemens PLCSim.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://www.automatak.com/opendnp3/" target="_blank">Opendnp3</a>
        </td>
        <td>
            Opendnp3 is the de facto reference implementation of IEEE-1815 (DNP3) provided under the Apache License.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://github.com/SCADACS/PLCinject" target="_blank">PLCinject</a>
        </td>
        <td>
            PLCinject can be used to inject code into PLCs.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://github.com/yanlinlin82/plcscan" target="_blank">plcscan</a>
        </td>
        <td>
            Tool for scaning PLC devices over the s7comm or modbus protocol.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://www.digitalbond.com/tools/quickdraw/download/" target="_blank">Quickdraw IDS</a>
        </td>
        <td>
            The Quickdraw IDS project by Digital Bond includes Snort rules for SCADA devices and so-called preprocessors for network traffic. 
            The preprocessors provide significant additional value because of their ability to reconstruct the protocol and state for use by Snort.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://github.com/0xICF/SCADAShutdownTool" target="_blank">SCADAShutdownTool</a>
        </td>
        <td>
            SCADAShutdownTool is an industrial control system automation and testing tool allows security researchers and experts to test SCADA security systems, enumerate slave controllers, read controller's registers values and rewrite registers data. 
        </td> 
    </tr>
    <tr>
        <td>
            <a href="http://snap7.sourceforge.net/" target="_blank">Snap7</a>
        </td>
        <td>
            Snap7 is an open source, 32/64 bit, multi-platform Ethernet communication suite for interfacing natively with Siemens S7 PLCs. The new CPUs 1200/1500, the old S7200, the small LOGO 0BA7/0BA8 and SINAMICS Drives are also partially supported.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="/source/s7-cracker.py" target="_blank">S7 Password Bruteforcer</a>
        </td>
        <td>
            A tool to bruteforce the password used by S7 instances from a PCAP using a dictionary. <a href="/source/s7-brute-offline.py" target="_blank">Original</a> created by SCADAStrangelove.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://splone.com/splonebox/" target="_blank">splonebox</a>
        </td>
        <td>
            splonebox is an open source network assessment tool with focus on modularity. It offers an ongoing analysis of a network and its devices. One major design decision features development of custom plugins, including ones for industrial communication protocols.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://www.wireshark.org/" target="_blank">Wireshark</a>
        </td>
        <td>
            Wireshark is the world's foremost network protocol analyzer. It lets you see what's happening on your network at a microscopic level. It is the de facto (and often de jure) standard across many industries and educational institutions. It has support for many protocols used in ICS.
        </td> 
    </tr>
</table>

## Distributions

<table>
    <tr>
        <td>
            <a href="https://github.com/moki-ics/moki" target="_blank">Moki Linux</a>
        </td>
        <td>
            Moki is a modification of Kali to encorporate various ICS/SCADA Tools scattered around the internet, to create a customized Kali Linux geared towards ICS/SCADA pentesting professionals.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="http://www.samuraistfu.org/" target="_blank">SamuraiSTFU</a>
        </td>
        <td>
            SamuraiSTFU takes the best in breed security tools for traditional network and web penetration testing, adds specialized tools for embedded and RF testing, and mixes in a healthy dose of energy sector context, documentation, and sample files, including emulators for SCADA, Smart Meters, and other types of energy sector systems to provide leverage a full test lab.
        </td> 
    </tr>
</table>

## Honeypots

<table>
    <tr>
        <td>
            <a href="https://github.com/mushorg/conpot" target="_blank">Conpot</a>
        </td>
        <td>
            Conpot is a low interactive server side Industrial Control Systems honeypot designed to be easy to deploy, modify and extend.
            It features easy customization and and behaviour mimicking, amongst others, and can be extended with real HMIs.
            Built and maintained under the Honeynet project.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://github.com/sjhilt/GasPot" target="_blank">GasPot</a>
        </td>
        <td>
            GasPot is a honeypot that has been designed to simulate a Veeder Root Gaurdian AST. These Tank Gauges are common in the oil and gas industry for Gas Station tanks to help with Inventory of fuels. GasPot was designed to randomize as much as possible so no two instances look exactly the same.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://dtag-dev-sec.github.io/mediator/feature/2016/03/11/t-pot-16.03.html" target="_blank">T-Pot</a>
        </td>
        <td>
            T-Pot is a combination of several honeypots that run in docker containers. Suricata and the ELK stack are used for security monitoring and visualization.
            Amongst others, it features Conpot and eMobility, which are an ICS and next generation transport infrastructure honeypots.
        </td> 
    </tr>
</table>

## Data

<table>
    <tr>
        <td>
            <a href="http://www.netresec.com/?page=PCAP4SICS" target="_blank">4SICS ICS Lab PCAPS</a>
        </td>
        <td>
            The "Geek Lounge" at 4SICS contains an ICS lab with PLCs, RTUs, servers, industrial network equipment (switches, firewalls, etc). These devices are available for hands-on "testing" by 4SICS attendees and traffic has been captured from these.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://media.defcon.org/DEF%20CON%2023/DEF%20CON%2023%20villages/DEF%20CON%2023%20ics%20village/DEF%20CON%2023%20ICS%20Village%20packet%20captures.rar" target="_blank">DEF CON 23 ICS Village PCAPS</a>
        </td>
        <td>
            PCAPS from the 23rd DEF CON.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://icsmap.shodan.io/" target="_blank">ICS Map</a>
        </td>
        <td>
            A map created from data gathered by Shodan showing ICS devices. Data is made available for further analysis.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://ics-radar.shodan.io/" target="_blank">ICS Radar</a>
        </td>
        <td>
            Data gathered from several types of ICS protocols by Shodan visualized on a globe.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://www.digitalbond.com/s4/s4x15-week/s4x15-ics-village/" target="_blank">S4x15 ICS Village</a>
        </td>
        <td>
            PCAPS from the S4x15 CTF as used during the contest.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://sourceforge.net/projects/s7commwireshark/files/Sample-captures/" target="_blank">S7 PCAP samples</a>
        </td>
        <td>
            Sample files for Wireshark S7 protocol dissector plugin.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://github.com/scadastrangelove/SCADAPASS" target="_blank">SCADAPASS</a>
        </td>
        <td>
            The famous SCADA StrangeLove Default/Hardcoded Passwords List.
        </td> 
    </tr>
</table>

## Feeds and News

<table>
    <tr>
        <td>
            <a href="https://ics-cert.us-cert.gov/alerts" target="_blank">ICS-CERT Alerts</a>
        </td>
        <td>
            The ICS-CERT Alert feed is intended to provide timely notification to critical infrastructure owners and operators concerning threats or activity with the potential to impact critical infrastructure computing networks.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://ics-cert.us-cert.gov/xml/rss.xml" target="_blank">ICS-CERT RSS Feed</a>
        </td>
        <td>
            The RSS feed by the United States ICS-CERT lists news and newly released vulnerability advisories.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="http://www.industry.siemens.com/topics/global/en/industrial-security/news-alerts/pages/alerts.aspx" target="_blank">Industrial Security Alerts</a>
        </td>
        <td>
            Siemens provides alerts for its industrial systems via this page and RSS feed.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="http://www.nerc.com/pa/rrm/bpsa/Pages/Alerts.aspx" target="_blank">North American Electric Reliability Corporation (NERC) Alerts</a>
        </td>
        <td>
            NERC provides alerts for Bulk Electric System (BES) security advisories and industry recommendations.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="http://new.abb.com/about/technology/cyber-security/alerts-and-notifications" target="_blank">ABB Cybersecurity Alerts and Notifications</a>
        </td>
        <td>
            ABB provides alerts for its cyber security incidents and software vulnerabilities.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="http://software.schneider-electric.com/support/cyber-security-updates/" target="_blank">Schneider Electric Cybersecurity Alerts and Notifications</a>
        </td>
        <td>
            Get the latest updates and alerts on Cyber Security and Compliance from Schneider Electric Software.
        </td> 
    </tr>
</table>



## Conferences and Conference Material

<table>
    <tr>
        <td>
            <a href="https://4sics.se/" target="_blank">4SICS</a>
        </td>
        <td>
            4SICS – Stockholm annual, international summit on cyber-security in SCADA and Industrial Control Systems.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="http://ics.sans.org/ics-library/summit-archives" target="_blank">SANS ICS Summit Archives</a>
        </td>
        <td>
            Central repository for the presentation material for the SANS ICS Summits held worldwide. 
        </td> 
    </tr>
    <tr>
        <td>
            <a href="http://www.icscybersecurityconference.com/" target="_blank">SANS ICS Cybersecurity Conference (WeissCon)</a>
        </td>
        <td>
            Affectionately known as WeissCon after it’s founder Joe Weiss, the conference is now owned and operated by SecurityWeek and usually runs in October at different locations each year in the US. 
        </td> 
    </tr>
</table>

## Literature

<table>
    <tr>
        <td>
            <a href="https://scadahacker.com/library/index.html" target="_blank">Library of Resources for
Industrial Control System Cyber Security</a>
        </td>
        <td>
            SCADAhacker.com's ultimate list of ICS/SCADA cybersecurity resources.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="http://www.amazon.com/Applied-Cyber-Security-Smart-Grid/dp/1597499986/" target="_blank">Applied Cyber Security and the Smart Grid</a>
        </td>
        <td>
            Applied Cyber Security and the Smart Grid: Implementing Security Controls into the Modern Power Infrastructure by Eric D. Knapp and Raj Samani.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://documents.trendmicro.com/assets/wp/wp-hacker-machine-interface.pdf" target="_blank">Hacker Machine Interface - The State of SCADA HMI Vulnerabilities</a>
        </td>
        <td>
            A TrendLabs Research Paper from the Trend Micro Zero Day Initiative Team about the current state of SCADA and HMI security.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://www.amazon.com/Handbook-Control-Systems-Security-Second/dp/1498717071/ref=sr_1_5?s=books&ie=UTF8&qid=1472416488&sr=1-5&keywords=scada+security" target="_blank">Handbook of SCADA/Control Systems Security</a>
        </td>
        <td>
            This comprehensive handbook covers fundamental security concepts, methodologies, and relevant information pertaining to supervisory control and data acquisition (SCADA) and other industrial control systems used in utility and industrial facilities worldwide.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="http://www.isaca.org/Journal/archives/2014/Volume-1/Documents/SCADA-Cybersecurity-Framework_joa_Eng_0114.pdf" target="_blank">SCADA Cybersecurity Framework</a>
        </td>
        <td>
            Paper describing what a SCADA Cyber Security framework should consist of.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="http://www.amazon.com/Industrial-Network-Security-Second-Edition/dp/0124201148/ref=sr_1_3?ie=UTF8&qid=1414970315&sr=8-3&keywords=industrial+network+security" target="_blank">Industrial Network Security, Second Edition</a>
        </td>
        <td>
            Industrial Network Security, Second Edition: Securing Critical Infrastructure Networks for Smart Grid, SCADA, and Other Industrial Control Systems by Eric D. Knapp and Joel Thomas Langill.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="http://www.amazon.com/Power-System-SCADA-Smart-Grids/dp/148222674X" target="_blank">Power System SCADA and Smart Grids</a>
        </td>
        <td>
            The book brings together in one concise volume the fundamentals and possible application functions of power system supervisory control and data acquisition (SCADA). Not security-oriented and geared towards power systems, but a good primer into SCADA nonetheless.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r2.pdf" target="_blank">NIST SP 800-82, Revision 2</a>
        </td>
        <td>
            Guide to Industrial Control Systems (ICS) Security by NIST.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://www.sans.org/reading-room/whitepapers/ICS/industrial-control-system-cyber-kill-chain-36297" target="_blank">The Industrial Control System Cyber Kill Chain</a>
        </td>
        <td>
            This SANS paper describes the ICS Cyber Kill Chain. It tailors the Lockheed Martin Kill Chain to typical, two phase attacks on ICS systems. 
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://ics.sans.org/media/An-Abbreviated-History-of-Automation-and-ICS-Cybersecurity.pdf" target="_blank">An Abbreviated History of Automation, Industrial Control Systems, and Cybersecurity</a>
        </td>
        <td>
            This SANS paper looks at the background on ICS cybersecurity. Well worth the read to make sure you understand many of the events that have occurred over the past twenty years and how they’ve inspired security in ICS today. 
        </td> 
    </tr>
    <tr>
        <td>
            <a href="http://www.controleng.com/networking-security/cyber-security.html" target="_blank">Control Engineering - Networking and Security - CyberSecurity</a>
        </td>
        <td>
            Control Engineering magazine's cybersecurity news and literature. 
        </td> 
    </tr>
</table>

## Introduction to ICS, SCADA, & PLCs

<table>
<tr>
        <td>
            <a href="http://plc-training.org/plc-network-to-hmi-scada.html" target="_blank">PLC Training Org</a>
        </td>
        <td>
            Site organizes all essential topics related to PLC training up to SCADA systems. While security is interwoven within the 10 learning phases, this is a great security article on the site for those just starting out.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://www.youtube.com/watch?v=VQLRVjEFRGI" target="_blank">Control System Basics</a>
        </td>
        <td>
            YouTube video explaining control system basics including the type of logic these systems use to sense and create physical changes to take action upon.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://www.youtube.com/watch?v=vv2CoTiaWPI" target="_blank">SCADA Systems - Utility 101 Session with Rusty Wiliiams</a>
        </td>
        <td>
            Utility industry professional Rusty Williams explains SCADA from an electric utility perspective.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://www.youtube.com/user/ControlLectures" target="_blank">Control System Lectures</a>
        </td>
        <td>
            Brian Douglas YouTube video series where he covers a wide range of topics on control systems in a very easy to process way.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://www.youtube.com/user/plcprofessor" target="_blank">The PLC Professor</a>
        </td>
        <td>
            The PLC Professor and his website plcprofessor.com contains a lot of great resources for learning what programmable logic controllers (PLCs) and other types of control systems and their logic are and how they work.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://www.youtube.com/watch?v=2DQdEHvnqvI" target="_blank">Serial Communications RS232 and RS485</a>
        </td>
        <td>
            John Rinaldi of Real Time Automation describes Serial communications RS232 and RS485.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://www.youtube.com/watch?v=OvRD2UvrHjE" target="_blank">All You Need To Know About MODBUS-RTU</a>
        </td>
        <td>
            John Rinaldi of Real Time Automation describes MODBUS-RTU.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://www.youtube.com/watch?v=8FYFai21JPA" target="_blank">MODBUS Data Structures</a>
        </td>
        <td>
            John Rinaldi of Real Time Automation describes MODBUS data structures.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://www.youtube.com/watch?v=E1nsgukeKKA" target="_blank">All You Need to Know About MODBUS-TCP</a>
        </td>
        <td>
            John Rinaldi of Real Time Automation describes MODBUS-TCP.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://www.youtube.com/watch?v=DL_zIjhCEpU" target="_blank">How Ethernet TCP/IP is Used by Industrial Protocols</a>
        </td>
        <td>
            John Rinaldi of Real Time Automation describes Ethernet TCP/IP.
        </td> 
    </tr>
</table>    

## License

Licensed under [Apache License 2.0](LICENSE).
