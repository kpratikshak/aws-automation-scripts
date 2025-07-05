#Network scanning script using nmap and XSLT transformation to HTML
import subprocess
import os
from lxml import etree

def main():
    try:
        # Get user inputs
        iporh = input("Enter the IP or hostname: ").strip()
        if not iporh:
            print("Error: IP or hostname is required")
            return
        
        argument = input("Enter the argument (default is -sS): ").strip() or "-sS"
        port = input("Enter the port (default is 80): ").strip() or "80"
        
        # Validate port
        try:
            port_num = int(port)
            if not (1 <= port_num <= 65535):
                print("Error: Port must be between 1 and 65535")
                return
        except ValueError:
            print("Error: Port must be a valid number")
            return
        
        # Build and execute nmap command
        command = f"nmap {argument} {iporh} -p {port} -oX nmap_output.xml"
        print(f"Running command: {command}")
        
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Error running nmap: {result.stderr}")
            return
        
        # Check if output file was created
        if not os.path.exists("nmap_output.xml"):
            print("Error: nmap_output.xml was not created")
            return
        
        # Check if XSLT file exists
        if not os.path.exists("nmap.xslt"):
            print("Error: nmap.xslt file not found")
            print("You need to have the nmap.xslt stylesheet file in the current directory")
            return
        
        # Parse XSLT and create transformer
        print("Parsing XSLT stylesheet...")
        xslt_doc = etree.parse("nmap.xslt")
        xslt_transformer = etree.XSLT(xslt_doc)
        
        # Parse XML source document
        print("Parsing nmap output...")
        source_doc = etree.parse("nmap_output.xml")
        
        # Apply transformation
        print("Applying XSLT transformation...")
        output_doc = xslt_transformer(source_doc)
        
        # Write output to HTML file
        print("Writing HTML output...")
        with open("nmap_output.html", "wb") as output_file:
            output_doc.write(output_file, pretty_print=True, xml_declaration=True, encoding="UTF-8")
        
        print("Successfully converted nmap XML output to HTML")
        print("Output saved as: nmap_output.html")
        
    except FileNotFoundError as e:
        print(f"File not found error: {e}")
    except etree.XSLTParseError as e:
        print(f"XSLT parsing error: {e}")
    except etree.XMLSyntaxError as e:
        print(f"XML syntax error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()