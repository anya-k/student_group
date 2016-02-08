from django.db import connection
from django.template import Template, Context


class SQLLogMiddleware:
    def process_response(self, request, response):
        if response.status_code == 200:
            total_time = 0

            for query in connection.queries:
                query_time = query.get('time')
                if query_time is None:
                    query_time = query.get('duration', 0) / 1000
                total_time += float(query_time)

            s = '{0} queries run, total {1} seconds'.format(len(connection.queries), total_time)
            response.content = response.content.replace('</body>', s + '</body>')

        return response
