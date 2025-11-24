# awesome-industrial-control-system-security
A curated list of resources related to Industrial Control System (ICS) security.

Feel free to [contribute](CONTRIBUTING.md).


## Tools

<table>
    <tr>
        <td>
            <a href="https://gitlab.com/jhcastel/attkfinder" target="_blank">AttkFinder</a>
        </td>
        <td>
            AttkFinder is a tool that performs static program analysis of PLC programs, and
produce Data-oriented Attack vectors. In a nutshell, AttkFinder takes PLC programs written
under the standard IEC-61131-3 in xml-format or structured text,
and builds a Data-Flow graph (DFG), a Control-Flow graph (CFG) and translates the program
into a Structured Intermediate Representation Language (STIR) version. A symbolic
execution engine analyses the stir-version code searching for attack vectors that can be
exploited by a malicious actuator.​
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://github.com/cisagov/cset" target="_blank">CSET</a>
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
            <a href="https://github.com/fireeye/ics_mem_collect" target="_blank">ics_mem_collect</a>
        </td>
        <td>
            Memory collector for GE D20MX. The project itself can be extended to work with other devices.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://github.com/dark-lbp/isf" target="_blank">ISF</a>
        </td>
        <td>
            The Industrial Exploitation Framework (ISF) is an exploitation framework similar to Metasploit written in Python. It is based on the open source Routersploit tool. It contains exploits for several types of controllers, such as QNX, Siemens and Schneider devices and includes several scanners.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://github.com/w3h/isf" target="_blank">ISEF</a>
        </td>
        <td>
            The Industrial Security Exploitation Framework (ISEF) is an exploitation framework based on the Equation Group Fuzzbunch toolkit as released by Shadow Brokers. It's developed by the ICSMASTER Security Team.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://github.com/momalab/ICSREF" target="_blank">ICSREF</a>
        </td>
        <td>
            A modular framework that automates the reverse engineering process of CODESYS binaries compiled with the CODESYS v2 compiler.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://github.com/momalab/ICSFuzz" target="_blank">ICSFuzz</a>
        </td>
        <td>
            A PLC-side fuzzing tool for uncovering vulnerabilities in ICS control applications. The current version supports only applications based on the Codesys platform which has been modified and adapted for the Wago PLC.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://github.com/woj-ciech/Kamerka-GUI" target="_blank">ꓘamerka GUI</a>
        </td>
        <td>
            Ultimate Internet of Things/Industrial Control Systems reconnaissance tool. 
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
            <a href="https://github.com/0x0mar/smod" target="_blank">MODBUS Penetration Testing Framework</a>
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
            <a href="https://dnp3.github.io/" target="_blank">OpenDNP3</a>
        </td>
        <td>
            OpenDNP3 is the de facto reference implementation of IEEE-1815 (DNP3) provided under the Apache License.
            It is currently in maintenance-only mode and new features are no longer being added. 
            Automatak has rebranded as Step Function I/O and is now focused on writing protocol <a href="https://stepfunc.io/products/libraries/" target="_blank">libraries</a> in Rust.
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
            <a href="https://github.com/dw2102/S7Comm-Analyzer" target="_blank">S7Comm-Analyzer</a>
        </td>
        <td>
            A plugin for Bro that parses S7comm protocol data traffic.
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
            <a href="https://github.com/mssabr01/sixnet-tools" target="_blank">sixnet-tools</a>
        </td>
        <td>
            Tool for exploiting Sixnet RTUs. This simple command line interface allows using undocumented function codes to gain root access anc control the underlying Linux OS on certain Sixnet family industrial control devices.
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
            <a href="https://github.com/klsecservices/s7scan" target="_blank">s7scan</a>
        </td>
        <td>
            A tool written in Python that scans networks, enumerates Siemens PLCs and gathers basic information about them, such as PLC firmware and hardware version, network configuration and security parameters.
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
    <tr>
        <td>
            <a href="https://github.com/otoriocyber/PCS7-Hardening-Tool" target="_blank">PCS7-Hardening-Tool</a>
        </td>
        <td>
            A standalone PowerShell script that enumerates security issues on Siemens PCS 7 DCS servers, based on Siemens security guides. created by OTORIO
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
            <a href="https://www.controlthings.io/" target="_blank">ControlThings Platform(Previously SamuraiSTFU)</a>
        </td>
        <td>
            The ControlThings Platform is an open source linux distribution for ICS cyber security teams. It takes the best-in-breed security assessment tools for traditional IT infrastructures and adds specialized tools for embedded electronics, proprietary wireless, and a healthy dose of ICS specific assessment tools, both from the community and custom tools created by the ControlThings I/O teams.
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
            <a href="https://github.com/automayt/ICS-pcap" target="_blank">ICS PCAP Collection by Jason Smith</a>
        </td>
        <td>
            A collection of PCAPs for various ICS utilities and protocols.
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
            <a href="https://www.netresec.com/?page=DigitalBond_S4" target="_blank">S4x15 ICS Village</a>
        </td>
        <td>
            Mirror for the PCAPS from the S4x15 CTF as used during the contest.
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
    <tr>
        <td>
            <a href="https://github.com/ICSrepo/TRISIS-TRITON-HATMAN" target="_blank">TRISIS/TRITON/HATMAN malware repository</a>
        </td>
        <td>
            Repository containting original and decompiled files of TRISIS/TRITON/HATMAN malware targeting Triconex Safety Instrumented System (SIS) controllers.
        </td> 
    </tr>   
    <tr>
        <td>
            <a href="https://github.com/gkabasele/HVAC_Traces" target="_blank">HVAC Traces</a>
        </td>
        <td>
           A repository that contains PCAP traces from a HVAC system of a university that can be used to ealuate Network Intrustion Detection Systems.
        </td> 
    </tr>
    
</table>

## Frameworks

<table>
    <tr>
        <td>
	    <a href="https://github.com/nathanpocock/I-ISMS" target="_blank">I-ISMS</a>
        </td>
        <td>
	    The Industrial Information Security Management System (I-ISMS) can be used to rapidly deploy an information security management program in an industrial setting. It provides templates for creating and implementing a program starting from the basics.
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
            <a href="https://new.siemens.com/global/en/products/services/cert.html" target="_blank">Industrial Security Alerts</a>
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
            <a href="https://cs3sthlm.se/" target="_blank">CS3STHLM</a>
        </td>
        <td>
             the Stockholm international summit on Cyber Security in SCADA and Industrial Control Systems - is an annual summit that gather the most important stakeholders across critical processes and industries. CS3STHLM has been organized since 2014, and has quickly become the premier ICS Security Summit in Northern Europe.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://cs3sthlm.se/" target="_blank">CS4CA</a>
        </td>
        <td>
             Cyber Security for Critical Assets is a global series of summits focusing on cyber security for critical infrastructure.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://www.sans.org/cyber-security-summit/archives" target="_blank">SANS ICS Summit Archives</a>
        </td>
        <td>
            Central repository for the presentation material for the SANS ICS Summits held worldwide (interleaved with other summits). 
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
    <tr>
        <td>
            <a href="https://ics.kaspersky.com/conference/" target="_blank">Kaspersky Industrial Cybersecurity conference (KICS con)</a>
        </td>
        <td>
            An annual international industrial cybersecurity conference run by Kaspersky.  
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://iccps.acm.org/" target="_blank">ICCPS: ACM/IEEE International Conference on Cyber-Physical Systems</a>
        </td>
        <td>
            The objective of ICCPS, the ACM/IEEE International Conference on Cyber-Physical Systems, is to serve as a single-track forum for reporting advances in all aspects of cyber-physical systems, including but not limited to theory, tools, applications, systems, and testbeds.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://www.acsac.org/2024/workshops/icss/" target="_blank">Industrial Control System Security (ICSS) Workshop</a>
        </td>
        <td>
            The goal of this workshop is to explore new techniques to improve security-critical control systems in the face of emerging threats.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://conferences.ds.unipi.gr/cybericps2025/" target="_blank">Workshop on the Security of Industrial Control Systems & of Cyber-Physical Systems (CyberICPS)</a>
        </td>
        <td>
            CyberICPS intends to bring together researchers, engineers and governmental actors with an interest in the security of ICS and CPS in the context of their increasing exposure to cyber-space, by offering a forum for discussion on all issues related to their cyber security.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://cpsiotsec.github.io/" target="_blank">Workshop on CPS & IoT Security and Privacy (CPSIoTSec)</a>
        </td>
        <td>
            Joint Workshop on CPS&IoT Security and Privacy that aims to present work done in the areas of tackling security and privacy issues for CPS and IoT.
    </tr>
    <tr>
        <td>
            <a href="http://jianying.space/cpss/CPSS2025/" target="_blank">ACM Cyber-Physical System Security Workshop (CPSS 2025)</a>
        </td>
        <td>
            This workshop will provide a platform for professionals from academia, government, and industry to discuss novel ways to address the ever-present security challenges facing CPS.
    </tr>
    <tr>
        <td>
            <a href="https://icps2025.ieee-ies.org/" target="_blank">IEEE Conference on Industrial Cyber-Physical Systems (ICPS) </a>
        </td>
        <td>
            This conference aims to provide a platform to exchange research and innovation results, as well as experiences learned from industrial practices associated with new paradigms and technologies related to Industrial Cyber-Physical Systems.
    </tr>
    <tr>
        <td>
            <a href="https://cns2024.ieee-cns.org/workshop/cps-sec-workshop" target="_blank">IEEE International Workshop on Cyber-Physical Systems Security (CPS-Sec)</a>
        </td>
        <td>
            CPS-Sec 2024 aims to serve as a platform for researchers and practitioners from both industry and academia interested in CPS security.
    </tr>
    <tr>
        <td>
            <a href="https://ricssworkshop.github.io" target="_blank">International Workshop on Re-design Industrial Control Systems with Security (RICSS)</a>
        </td>
        <td>
            While some proprietary ICS vendors have begun offering security solutions, free and open-source ICS software remains less recognized. The goal of the workshop is twofold: collecting ideas on redesigning (parts of) the ICS ecosystem; also inviting contributions on designing, incorporating, and maintaining secure open-source ICS software.
    </tr>
</table>

## Literature

<table>
    <tr>
        <td>
            <a href="https://collaborate.mitre.org/attackics/index.php/Main_Page" target="_blank">ATT&CK® for Industrial Control Systems by MITRE</a>
        </td>
        <td>
            ATT&CK for ICS is a knowledge base useful for describing the actions an adversary may take while operating within an ICS network.
        </td> 
    </tr>
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
            <a href="http://www.robertmlee.org/a-collection-of-resources-for-getting-started-in-icsscada-cybersecurity/" target="_blank">A Collection of Resources for Getting Started in ICS/SCADA Cybersecurity</a>
        </td>
        <td>
            Robert M. Lee's thoughts on some good resources on ICS & SCADA security.
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
    <tr>
       <td>
           <a href="https://www.fireeye.com/blog/threat-research/2019/09/ontology-understand-assess-operational-technology-cyber-incidents.html" target="_blank">Operational Technology Cyber Security Incidents Ontology (OT-CSIO)</a>
       </td>
       <td>
           OT-CSIO, created by FireEye, is an ontology to understand, cross-compare and assess cyber security incidents related to operational technology. It provides guidance for assessing risks and helps making informed decisions.
       </td>
    </tr>
    <tr>
       <td>
           <a href="https://www.newnettechnologies.com/downloads/Implementation-Guide-for-ICS-using-the-CIS-Controls.pdf" target="_blank">CIS Controls Implementation Guide for Industrial Control Systems - Version 7</a>
       </td>
       <td>
            This document provides guidance on how to apply the security best practices found in CIS Controls Version 7.1 to ICS environments.
       </td>
    </tr>
    <tr>
       <td>
           <a href="https://www.nrdcs.lt/file/repository/resources/CIS_Controls_IoT_Companion_Guide.pdf" target="_blank">CIS Controls Internet of Things Companion Guide - Version 7.1</a>
       </td>
       <td>
            The objective of this document is to have broad applicability across sectors. IoT affects all areas of computingacross multiple sectors, such as healthcare, aviation, public safety, and energy. This has led to sector-specific IoT security guidance, but this document is purposefully sector-agnostic.
       </td>
    </tr>
</table>


## Education

<table>
    <tr>
        <td>
            <a href="https://github.com/Fortiphyd/GRFICSv2" target="_blank">GRFICSv2</a>
        </td>
        <td>
            The second version of the Graphical Realism Framework for Industrial Control Simulations (GRFICS) is a framework for realistic industrial control simulations that uses Unity 3D game engine for simulating industrial control systems. GRFICS provides users with a full virtual industrial control system (ICS) network to practice common attacks including command injection, man-in-the-middle, and buffer overflows, and visually see the impact of their attacks in the 3D visualization. Users can also practice their defensive skills by properly segmenting the network with strong firewall rules, or writing intrusion detection rules. The first version can be found <a href="https://github.com/djformby/GRFICS" target="_blank">here</a>.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://github.com/hsainnos/LICSTER" target="_blank">LICSTER</a>
        </td>
        <td>
            LICSTER, the Low-cost ICS Security Testbed for Education and Research, aims to help setup a minimal, low-cost Industrial Control System (ICS) testbest for students, researchers, or anyone with an interest in industrial security. The project contains a list of affordable hardware to build the minimalistic ICS with, instructions, configurations and installation scripts to instantiate the system as well as various attacker scenarios and their implications. The paper can be found <a href="https://arxiv.org/abs/1910.00303", target="_blank">here</a>.
        </td> 
    </tr>
    <tr>
        <td>
            <a href="https://icscsi.org/" target="_blank">Industrial Control System Cyber Security Institute</a>
        </td>
        <td>
            The ICS Cyber Security Institute offers on-line training developed by practitioners in both ICS system design/operation and cyber security design/compliance. 
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
    <tr>
        <td>
            <a href="https://www.youtube.com/channel/UCUKKQwBQZczpYzETkZNxi-w" target="_blank">RealPars</a>
        </td>
        <td>
            The RealPars YouTube channel has many videos on industrial automation and PLC programming.
        </td> 
    </tr>
</table>    

## License

Licensed under [Apache License 2.0](LICENSE).
