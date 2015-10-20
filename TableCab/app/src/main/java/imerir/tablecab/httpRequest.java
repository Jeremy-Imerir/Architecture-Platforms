package imerir.tablecab;

import android.os.AsyncTask;
import android.util.Log;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.URL;

/**
 * Created by Brice-PC on 20/10/2015.
 */
public class httpRequest extends AsyncTask<String, Void, JSONObject> {

    public JSONObject jsonResult = null;

    @Override
    protected JSONObject doInBackground(String... params) {
        int length = 500;
        URL url = null;
        HttpURLConnection urlConnection = null;
        try {
            url = new URL("http://172.30.0.227:8090");
            urlConnection = (HttpURLConnection) url.openConnection();
            InputStream in = new BufferedInputStream(urlConnection.getInputStream());
            String stringGetFromHttp = convertInputStreamToString(in);
            Log.d("HTTP Request", stringGetFromHttp);

            JSONObject json = new JSONObject(stringGetFromHttp);

            this.jsonResult = json;
            return json;
        }
        catch (IOException e) {
            e.printStackTrace();
        } catch (JSONException e) {
            e.printStackTrace();
        } finally {
            urlConnection.disconnect();
        }
        return null;
    }

    protected void onPostExecute(Boolean result) {

    }

    public String convertInputStreamToString(InputStream stream) throws IOException, UnsupportedEncodingException {
        try {
            ByteArrayOutputStream bo = new ByteArrayOutputStream();
            int i = stream.read();
            while(i != -1) {
                bo.write(i);
                i = stream.read();
            }
            return bo.toString();
        } catch (IOException e) {
            return "";
        }
    }
}
