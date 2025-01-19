from mitmproxy import ctx
import json
import os
from datetime import datetime
import re
import urllib.parse

def clean_filename(url):
    # Extract just the carrera ID from the URL
    try:
        params = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
        carrera_id = params.get('idCarrera', ['unknown'])[0]
        # Remove any special characters and keep only alphanumeric
        clean_id = re.sub(r'[^a-zA-Z0-9]', '', carrera_id)
        return clean_id
    except:
        # If anything goes wrong, return a timestamp
        return datetime.now().strftime("%Y%m%d_%H%M%S")

def response(flow):
    if "ObtenerListaOfertaDeMaterias" in flow.request.pretty_url:
        try:
            # Parse the JSON response
            response_data = json.loads(flow.response.content)
            
            # Create directory if it doesn't exist
            output_dir = "json_responses"
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            # Generate a clean filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            clean_id = clean_filename(flow.request.pretty_url)
            filename = f"{output_dir}/response_{timestamp}_carrera_{clean_id}.json"
            
            # Save the JSON response
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(response_data, f, ensure_ascii=False, indent=4)
            
            ctx.log.info(f"Saved JSON response to {filename}")
            
        except json.JSONDecodeError:
            ctx.log.error(f"Response was not valid JSON for URL: {flow.request.pretty_url}")
        except Exception as e:
            ctx.log.error(f"Error processing response: {str(e)}\nURL: {flow.request.pretty_url}")