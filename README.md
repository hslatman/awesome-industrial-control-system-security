# awesome-industrial-control-system-security
A curated list of resources related to Industrial Control System (ICS) security.

Feel free to [contribute](CONTRIBUTING.md).


## Tools

<table>
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
            <a href="https://github.com/enddo/smod" target="_blank">MODBUS Penetration Testing Framework</a>
        </td>
        <td>
            smod is a modular framework with every kind of diagnostic and offensive feature you could need in order to pentest modbus protocol. It is a full Modbus protocol implementation using Python and Scapy. The framework can be used to perform vulnerability assessments.
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
            <a href="https://www.digitalbond.com/s4/s4x15-week/s4x15-ics-village/" target="_blank">S4x15 ICS Village</a>
        </td>
        <td>
            PCAPS from the S4x15 CTF as used during the contest.
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
</table>

## Literature

<table>
    <tr>
        <td>
            <a href="http://csrc.nist.gov/publications/nistpubs/800-82/SP800-82-final.pdf" target="_blank">SP 800-82</a>
        </td>
        <td>
            The Guide to Industrial Control Systems (ICS) Security by NIST.
        </td> 
    </tr>
</table>

## License

Licensed under [Apache License 2.0](LICENSE).