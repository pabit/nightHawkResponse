import elasticsearch
from elasticsearch_dsl import Search, Q, A

def GetGeneratorQuery(auditgenerator_type, str_query, case, endpoint_id, start, length, sort, order):
	s = Search()
	s = s[int(start):int(length)+int(start)]

	if auditgenerator_type == "w32registryraw":
		order_dict = {
			"0": "Modified",
			"1": "Path",
			"2": "Type",
			"3": "Text",
			"4": "Bytes",
			"5": "Hive",
			"6": "Username",
			"7": "JobCreated",
			"8": "ValueName",
			"9": "IsKnownKey",
			"10": "KeyPath",
			"11": "SecurityID",
			"12": "Tag",
			"13": "Comment",
			"14": "nHscore"
		}
		if str_query == "":
			_sort = {
				"Record.{0}".format(order_dict[str(sort)]): {
					"order": order
				}
			}

			t = Q('query_string', default_field="ComputerName", query=endpoint_id) & Q('query_string', default_field="CaseInfo.case_name", query=case)
			query = s.query(t).filter('term', AuditType__Generator=auditgenerator_type).sort(_sort)

		else:
			_sort = {
				"Record.{0}".format(order_dict[str(sort)]): {
					"order": order
				}
			}

			t = Q('query_string', default_field="ComputerName", query=endpoint_id) & Q('query_string', default_field="CaseInfo.case_name", query=case) & Q('query_string', fields=["Record.Path", "Record.Username", "Record.ValueName", "Record.Text", "Record.Tag", "Record.Comment"], query="{0}".format(str_query))
			query = s.query(t).filter('term', AuditType__Generator=auditgenerator_type).sort(_sort)

		return query

	elif auditgenerator_type == "filedownloadhistory":
		order_dict = {
			"0": "LastModifiedDate",
			"1": "SourceUrl",
			"2": "Filename",
			"3": "Username",
			"4": "DownloadType",
			"5": "Profile",
			"6": "BrowserName",
			"7": "BrowserVersion",
			"8": "TargetDirectory",
			"9": "FullHttpHeader",
			"10": "LastCheckedDate",
			"11": "BytesDownloaded",
			"12": "CacheFlags",
			"13": "IsGoodFile",
			"14": "Tag",
			"15": "Comment",
			"16": "nHscore"
		}
		if str_query == "":
			_sort = {
				"Record.{0}".format(order_dict[str(sort)]): {
					"order": order
				}
			}

			t = Q('query_string', default_field="ComputerName", query=endpoint_id)
			query = s.query(t).filter('term', AuditType__Generator=auditgenerator_type).sort(_sort)

		else:
			_sort = {
				"Record.{0}".format(order_dict[str(sort)]): {
					"order": order
				}
			}
			t = Q('query_string', default_field="ComputerName", query=endpoint_id) & Q('query_string', fields=["Record.SourceUrl", "Record.Username", "Record.TargetDirectory", "Record.FullHttpHeader", "Record.Filename", "Record.BrowserName", "Record.Profile", "Record.Tag", "Record.Comment"], query="{0}".format(str_query))
			query = s.query(t).filter('term', AuditType__Generator=auditgenerator_type).sort(_sort)

		return query

	elif auditgenerator_type == "urlhistory":
		order_dict = {
			"0": "LastVisitDate",
			"1": "Hidden",
			"2": "Username",
			"3": "Url",
			"4": "BrowserName",
			"5": "BrowserVersion",
			"6": "PageTitle",
			"7": "VisitFrom",
			"8": "VisitType",
			"9": "IsGoodDomain",
			"10": "IsNewDomain",
			"11": "nHscore",
			"12": "Tag",
			"13": "Comment"
		}
		if str_query == "":
			_sort = {
				"Record.{0}".format(order_dict[str(sort)]): {
					"order": order
				}
			}

			t = Q('query_string', default_field="ComputerName", query=endpoint_id)
			query = s.query(t).filter('term', AuditType__Generator=auditgenerator_type).sort(_sort)

		else:
			_sort = {
				"Record.{0}".format(order_dict[str(sort)]): {
					"order": order
				}
			}
			
			t = Q('query_string', default_field="ComputerName", query=endpoint_id) & Q('query_string', fields=["Record.Url", "Record.Username", "Record.Profile"], query="{0}".format(str_query))
			query = s.query(t).filter('term', AuditType__Generator=auditgenerator_type).sort(_sort)

		return query