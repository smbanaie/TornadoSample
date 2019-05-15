from  ebaysdk import trading
import base64
class trading_multipart( trading ):
    """
    Modified 'trading' class for handling multipart post with mime sections.
    """

    # same as 'trading' except take image data (base64 encoded) as extra parameter
    def execute( self, verb, xml, imgdata_base64 ):
        self.boundary       = 'MIME_boundary'
        self.imgdata_base64 = imgdata_base64
        self.mpxml          = None
        super( trading_multipart, self ).execute( verb, xml )

    # same as 'trading' except the 'Content-Type' header
    def _build_request_headers( self ):
        headers = super( trading_multipart, self )._build_request_headers()
        headers['X-EBAY-API-COMPATIBILITY-LEVEL'] = '759'
        # override the default content type only if mutltipart will be necessary
        if self.imgdata_base64 != '':
            headers['Content-Type'] = 'multipart/form-data; charset=UTF-8; boundary=' + self.boundary

        # construct the request body because we need to provide the content length
        self._build_request_xml()
        headers['Content-Length'] = '%s' % len( self.mpxml )

        return headers

    # construct a simple XML or a multipart post
    def _build_request_xml( self ):

        # if we have constructed the XML already, just return it
        if self.mpxml is not None:
            return self.mpxml

        xml = super( trading_multipart, self )._build_request_xml()

        # if we don't have to do the image data / multipart, we're done
        if self.imgdata_base64 == '':
            self.mpxml = xml
            return self.mpxml

        # multipart POST consists of an XML request plus the base64 image separated by boundaries

        CRLF = "\r\n"

        part1  = "--" + self.boundary + CRLF
        part1 += 'Content-Disposition: form-data; name=document' + CRLF
        part1 += 'Content-Type: text/xml; charset="utf-8"' + CRLF + CRLF
        part1 += xml
        part1 += CRLF

        part2  = "--" + self.boundary + CRLF
        part2 += 'Content-Disposition: form-data; name=image; filename=image' + CRLF
        #part2 += "Content-Transfer-Encoding: base64" + CRLF
        part2 += "Content-Transfer-Encoding: Binary" + CRLF
        part2 += "Content-Type: application/octet-stream" + CRLF + CRLF
        #part2 += self.imgdata_base64

        # in order to mix the text with the binary contents of the picture file
        # we will open a temp file for binary write and read back from it
        tmpfile = '/tmp/%s.bin' % random.randint( 0, 100000 )
        f = open( tmpfile, 'wb' )
        f.write( part1 )
        f.write( part2 )
        f.write( base64.b64decode( self.imgdata_base64 ) )
        f.write( CRLF )
        f.write( "--" + self.boundary + "--" + CRLF )
        f.close()
        # read back what we wrote to the file
        f = open( tmpfile, 'rb' )
        self.mpxml = f.read()
        f.close()
        # we don't need the file anymore, try to delete it
        try:
            os.remove( tmpfile )
        except Exception as  e:
            pass

        return self.mpxml